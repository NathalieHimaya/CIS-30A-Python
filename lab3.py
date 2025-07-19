# # Lab 3 Ex. 1

# A_set = frozenset([100, 200, 300])
# B_set = frozenset([300, 400, 500])
# C_set = frozenset([500, 600, 700])

# one = A_set.intersection(B_set)
# print(one)

# two = A_set.difference(B_set)
# print(two)

# three = A_set.isdisjoint(B_set)
# print(three)

# four = A_set.union(B_set)
# print (four)

# five = B_set.symmetric_difference(C_set)

# # Ex. 2

# letters_1 = {'D', 'E', 'F', 'G'}
# letters_2 = {'H', 'I'}

# letters_3 = letters_1.copy()
# print(letters_1)

# letters_1.update(letters_2)
# print (letters_1)

# differance = letters_1.difference(letters_2)
# print(differance)

# letters_1.remove('I')
# print(letters_1)

# print(len(letters_1))

# letters_1.discard('I')
# letters_1.discard('E')
# print(letters_1)

# # Ex. 3
# import collections

# months_Dq = collections.deque(['Mar', 'April', 'May'])

# # A - adds to the end
# months_Dq.extend(['June', 'July', 'August'])
# print(months_Dq)

# # B - adds from the left starting feb jan dec mar
# months_Dq.appendleft(['Dec', 'Jan', 'Feb'])
# print(months_Dq)

# # C - removes last item from left "Feb"
# months_Dq.popleft()
# print(months_Dq)

# # D - Removes last item from the right side "August"
# months_Dq.pop()
# print(months_Dq)

# #E - removes the occurance of the string
# months_Dq.remove('June')
# print(months_Dq)

# Ex. 4

# #creating a set
# carolina = set([92, 87, 93, 88])
# raquel = set([88, 92, 81, 97])

# # symmetric.difference returns values that are in either set but not both
# diff = carolina.symmetric_difference(raquel)
# print(diff)

# # display same quiz score using .intersection() returns values that are common to both sets
# common = carolina.intersection(raquel)

# # min(set_name) removes lowest number
# # .remove(name) deletes item from set

# carolina.remove(min(carolina))
# raquel.remove(min(raquel))

# print(carolina)
# print(raquel)

# # Ex. 5
# # a. Declare the given sets
# st_A = {'c', 'o', 'm', 'p', 'u', 't', 'e', 'r'}
# st_B = {'m', 'u', 't', 'e'}

# if st_B.issubset(st_A):
#     print("Set B is a subset of Set A")

# if st_A.issuperset(st_B):
#     print("Set A is a superset of Set B")

# # Ex. 6

# #function

# def mileseachday(miles):
#     km = [m * 1.6 for m in miles]
#     print("Your total miles is", sum(km))

# miles = [50, 70, 100]
# mileseachday(miles)

# # Ex. 7

# def oddoreven(number):
#     if number % 2 == 0:
#         print("This number is even")
#     else:
#         print("The number is odd")

# number = int(input("Enter a number: "))

# oddoreven(number)

# # Ex. 8

# import textinfo

# text = input("Enter a string: ")

# textinfo.lengthofstring(text)

# # Ex. 9
# f = open("myfile.txt", 'r')
# f.close

# # Ex. 10
# with open("myfile.txt", "r") as myfile:
#     content = myfile.read()
#     print("File Content:")
#     print(content)

#     myfile.seek(0) 
#     lines = myfile.readlines()
#     print("Total number of lines:", len(lines))

#     word_count = sum(len(line.split()) for line in lines)
#     print("Total number of words:", word_count)

# # Ex. 11
# import customer_module
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# phone = input("Enter your phone number: ")
# marital_status = input("Enter your marital status: ")

# if (customer_module.is_valid_input(name) and
#     customer_module.is_valid_input(age) and
#     customer_module.is_valid_input(phone) and
#     customer_module.is_valid_input(marital_status)):

#     customer_data = {
#         "Name": name,
#         "Age": age,
#         "Phone Number": phone,
#         "Marital Status": marital_status
#     }

#     customer_module.save_customer_info(customer_data)
#     customer_module.read_customer_info()

# else:
#     print("Invalid input detected. Only digits or alphabetic characters are allowed.")

# # Ex. 12

# subtotal = float(input("Enter the subtotal amount: $"))

# sales_tax = subtotal * 0.0775
# print(f"Sales tax amount: ${sales_tax:.2f}")

# shipping_cost = subtotal * 0.05
# print(f"Shipping cost: ${shipping_cost:.2f}")

# grand_total = subtotal + sales_tax + shipping_cost
# print(f"Grand total: ${grand_total:.2f}")

# product_choice = input("Enter product choice: ")
# discount = input("Enter discount (if any): ")

# with open("receipt.txt", "w") as receipt_file:
#     receipt_file.write(f"Product Choice: {product_choice}\n")
#     receipt_file.write(f"Discount: {discount}\n")
#     receipt_file.write(f"Subtotal: ${subtotal:.2f}\n")
#     receipt_file.write(f"Sales Tax: ${sales_tax:.2f}\n")
#     receipt_file.write(f"Shipping Cost: ${shipping_cost:.2f}\n")
#     receipt_file.write(f"Grand Total: ${grand_total:.2f}\n")

# print("Thank you for shopping with us!")

# # Ex. 13
# import receipt_module

# products = {
#     "1": ("Laptop", 299.99),
#     "2": ("Gaming desktop PC", 1029.99),
#     "3": ("TV", 249.99),
#     "4": ("X-box One", 219.99),
#     "5": ("Nintendo Switch", 279.99)
# }

# subtotal = 0.0
# order_list = []

# while True:
#     print("\nBestElectronics Menu:")
#     for key, value in products.items():
#         print(f"{key}. {value[0]}: ${value[1]:.2f}")

#     choice = input("Enter product number (1–5): ")
#     if choice in products:
#         item, price = products[choice]
#         order_list.append(item)
#         subtotal += price
#         print(f"{item} added to cart.")
#     else:
#         print("Invalid choice.")

#     another = input("Do you want to add another product? (yes/no): ").lower()
#     if another != "yes":
#         break

# tax = subtotal * 0.0775
# grand_total = subtotal + tax

# receipt_module.save_receipt(order_list, subtotal, tax, grand_total)
# receipt_module.display_receipt()

# print("Thank you for shopping with BestElectronics!")

# Ex. 14
prod = {'tomato': 'red', 'squash': 'yellow', 'potato': 'brown', 'avocado': 'green'}

def display_product_colors():
    for item, color in prod.items():
        print(f"'{item}': '{color}'")

def show_scope_details():
    print("\n--- GLOBAL VARIABLES ---")
    for key in globals():
        print(key)
    
    print("\n--- LOCAL VARIABLES ---")
    for key in locals():
        print(key)

display_product_colors()
show_scope_details()
