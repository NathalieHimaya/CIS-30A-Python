def is_valid_input(value):
    return value.isdigit() or value.isalpha()

def save_customer_info(info_dict):
    with open("customer_info.txt", "w") as file:
        for key, value in info_dict.items():
            file.write(f"{key}: {value}\n")

def read_customer_info():
    with open("customer_info.txt", "r") as file:
        data = file.read()
        print("\nStored Customer Information:")
        print(data)