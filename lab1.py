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

# # Exercise 6: Cloud Storage Cost using Variables and Operators

# datastored = int(input("Enter amount of data stored in cloud:"))
# additionaldata = (datastored - 750)
# extra_data_cost = round(additionaldata * 5)
# monthly_cost = round(extra_data_cost + 100)

# print("You have used an additional ", additionaldata, "GB")
# print("5", extra_data_cost, "will be added to your monthly cost")
# print("Your current monthly cost now $", monthly_cost)

# # Exercise 7: Square Footage Variables and Operators

# livinglength = int(input("Enter length of living room: "))
# livingwidth = int(input("Enter width of living room:"))
# masterlength = int(input("Enter length of master room: "))
# masterwidth = int(input("Enter width of master room:"))
# kitchenlength = int(input("Enter kitchen length of room: "))
# kitchenwidth = int(input("Enter kitchen width of room:"))


# area1 = livinglength * livingwidth
# area2 = masterlength * masterwidth
# area3 = kitchenlength * kitchenwidth

# totalarea = area1 + area2 + area3

# totalsqft = 4.57 * totalarea

# print("Your cost of flooring is: $", round(totalsqft))

# # Excerise 8: Using String Format, Variables to Determine Shipping

# tablet = 1
# laptop = 7
# tv = 37
# shippingrate = 2.66

# totalweight = tablet + laptop + tv
# shippingcost = shippingrate * totalweight

# print("Jack will spend ${} on shipping".format(shippingcost))

# # Exercist 9: Using abs()

# num = -288
# print(abs(num))

# Exercise 10: Using ceil() and floor in python math module

# import math

# jweight = 187.13

# print("This is Juan's weight using floor: ", math.floor(jweight))
# print("This is Juan's weight using ceil: ", math.ceil(jweight))

# # Exercise 11: Using min() and max() in Python

# quizscores = [90, 78, 82, 61, 87, 94]

# print("The highest score is ", max(quizscores))
# print("The lowest score is ", min(quizscores))

# Exercise 12: Using sum() to find total
miles = [2,3,5,8]
print(sum(miles, 10))
