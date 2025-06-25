# # Exercise 2
# print ("Exercise 1: Hello I'm Nathalie")

# # Exercise 3
# myname = "Nathalie"
# age = 21
# major = "Computer Science"

# print (myname)
# print (age)
# print (major)

# # Exercise 4
# user_name = input("Enter your name: ")
# user_age = input("Enter your age: ")
# user_height = input("Enter height: ")
# user_weight = input("Enter weight in lbs: ")

# print ( user_name, user_age, user_height, user_weight)

# # Exercise 5

# num1 = int(input("Number 1: "))
# num2 = int(input("Number 2: "))
# num3 = int(input("Number 3: "))
# num4 = int(input("Number 4: "))
# total = num1 + num2 + num3 + num4
# avg = total/4

# print ("Total: ", total)
# print ("Avg: ", avg)

# # Exercise 5: Unit Conversion

# heightin = int(input("Enter Height in inches: "))

# inchtometer = 39.37

# print ("Your height from inches to meters: ", heightin/inchtometer)

# Exercise 5: Cloud Storage Cost using Variables and Operators

datastored = int(input("Enter amount of data stored in cloud:"))
additionaldata = (datastored - 750)
extra_data_cost = round(additionaldata * 5)
monthly_cost = round(extra_data_cost + 100)

print("You have used an additional ", additionaldata, "GB")
print("5", extra_data_cost, "will be added to your monthly cost")
print("Your current monthly cost now $", monthly_cost)
