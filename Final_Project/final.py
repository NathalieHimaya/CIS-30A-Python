import datetime

# ALL OBJECTS AND METHODS HERE + Classes with Inheritance
class Utils:
    @staticmethod
    def format_price(price):
        return f"${price:.2f}" #String Object
    
    @staticmethod
    def validate_phone(phone):
        return len(phone.replace('-', '').replace(' ', '')) == 10

# Base class for menu items
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def total(self, qty):
        return self.price * qty

# Drink subclass
class Drink(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)
# Food subclass  
class Food(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

# Customer class
class Customer:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

# Order class
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.delivery_date = ""
        self.delivery_time = ""
        self.order_id = f"CAFE{datetime.datetime.now().strftime('%m%d%H%M')}"
        self.total = 0.0
    
    def add_item(self, item, qty):
        self.items.append({'name': item.name, 'qty': qty, 'subtotal': item.total(qty)})
        self.total += item.total(qty)
    
    def set_delivery(self, date, time):
        self.delivery_date = date
        self.delivery_time = time
    
    def summary(self):
        lines = ["=" * 30, "SUNRISE CAFE ORDER", "=" * 30, f"ID: {self.order_id}", ""]
        lines.append(f"Customer: {self.customer.name}")
        lines.append(f"Phone: {self.customer.phone}")
        lines.append(f"Address: {self.customer.address}")
        lines.append("")
        
        # Loop through items
        for i, item in enumerate(self.items, 1):
            lines.append(f"{i}. {item['name']} x{item['qty']} - {Utils.format_price(item['subtotal'])}")
        
        lines.append(f"\nTotal: {Utils.format_price(self.total)}")
        if self.delivery_date:
            lines.append(f"Delivery: {self.delivery_date} at {self.delivery_time}")
        lines.append("\nThank you!")
        return "\n".join(lines)

 # ERROR DETECTION IS HERE + FILE OPERATIONS
    def save_file(self):
        try:
            filename = f"order_{self.order_id}.txt"
            with open(filename, 'w') as f:
                f.write(self.summary())
            return filename
        except Exception as e:
            raise IOError(f"Save error: {e}")

# =================================
#  CUSTOMER INFORMATION IS HERE !!!
# =================================

def get_customer():
    print("=== Customer Info ===")
    while True:
        name = input("Name: ").strip()
        if name: break
        print("Name required!")
    
    while True:
        phone = input("Phone: ").strip()
        if Utils.validate_phone(phone): break
        print("Invalid phone!")
    
    while True:
        address = input("Address: ").strip()
        if address: break
        print("Address required!")
    
    return Customer(name, phone, address)

# =================================
#  MENU AND ORDERING WILL BE RIGHT HERE
# =================================
def create_menu():
    drinks = [Drink("Coffee", 3.50), Drink("Tea", 2.75), Drink("Latte", 4.25)]
    foods = [Food("Sandwich", 6.50), Food("Bagel", 3.25), Food("Cookie", 1.75)]
    return drinks + foods

# Take order function
def take_order(menu, order):
    while True:
        print(f"\n=== Menu === Total: {Utils.format_price(order.total)}")
        for i, item in enumerate(menu, 1):
            print(f"{i}. {item.name} - {Utils.format_price(item.price)}")
        
        try:
            choice = int(input("Item number (0 to finish): "))
            if choice == 0: break
            elif 1 <= choice <= len(menu):
                item = menu[choice - 1]
                while True:
                    try:
                        qty = int(input(f"Quantity of {item.name}: "))
                        if qty > 0: break
                        print("Must be positive!")
                    except ValueError:
                        print("Invalid number!")
                
                order.add_item(item, qty)
                print(f"Added {qty} {item.name}!")
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input!")

# THIS IS WHERE CUSTOMER SCHEDULES DELIVERY
def schedule_delivery(order):
    print("\n=== Delivery ===")
    
    while True:
        try:
            date_input = input("Delivery date (MM-DD): ")
            month, day = map(int, date_input.split('-'))
            
            if 1 <= month <= 12 and 1 <= day <= 31: # Validates the Date
                current_year = datetime.date.today().year
                test_date = datetime.date(current_year, month, day)
                
                # If date is in past, use next year
                if test_date < datetime.date.today():
                    test_date = datetime.date(current_year + 1, month, day)
                
                # Checks the date if its way past a year
                max_date = datetime.date.today() + datetime.timedelta(days=365)
                if test_date <= max_date:
                    formatted_date = f"{month:02d}-{day:02d}"
                    break
                else:
                    print("Date too far in future!")
            else:
                print("Invalid date!")
        except ValueError:
            print("Use MM-DD format!")
    
    # Customer will choose their time slot here for their delivery
    times = ["9:00 AM", "12:00 PM", "3:00 PM", "6:00 PM"]
    print("Times:")
    for i, time in enumerate(times, 1):
        print(f"{i}. {time}")
    
    while True:
        try:
            choice = int(input("Time choice (1-4): "))
            if 1 <= choice <= 4:
                order.set_delivery(formatted_date, times[choice - 1])
                print(f"Delivery: {formatted_date} at {times[choice - 1]}")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input!")

# ===========================================

#      MAIN FUCTION IS HERE

# ===========================================
def main():
    print("Welcome to Sunrise Cafe!")
    
    customer = get_customer()
    order = Order(customer)
    menu = create_menu()
    
    take_order(menu, order)
    
    if not order.items:
        print("No items ordered!")
        return
    
    schedule_delivery(order)
    print("\n" + order.summary())
    
    if input("\nSave to file? (y/n): ").lower() in ['y', 'yes']:
        try:
            filename = order.save_file()
            print(f"Saved: {filename}")
        except Exception as e:
            print(f"Error: {e}")

# Run program
if __name__ == "__main__":
    main()