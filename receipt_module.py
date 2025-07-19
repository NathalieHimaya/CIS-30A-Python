# receipt_module.py

def save_receipt(order_list, subtotal, tax, grand_total):
    with open("receipt.txt", "w") as file:
        file.write("Customer Order:\n")
        for item in order_list:
            file.write(f"- {item}\n")
        file.write(f"\nSubtotal: ${subtotal:.2f}\n")
        file.write(f"Sales Tax (7.75%): ${tax:.2f}\n")
        file.write(f"Grand Total: ${grand_total:.2f}\n")

def display_receipt():
    with open("receipt.txt", "r") as file:
        print("\n--- RECEIPT ---")
        print(file.read())
