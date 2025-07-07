# #String Sequencing and Built-in Methods
# #Ex. 1

# name = "Nathalie"

# print(name[0]," ",name[7] )
# print("The number of characters is my name is ", len(name))
# print(name[0], " ", name[2])
# print(name[1], " ", name[7])
# print(len(name[6]))


# # Ex. 2
# state_name = "Indianpolis"
# print(state_name.count("i"))

# # # Ex. 3
# thestring = 'I am a college student'
# print(thestring.replace("college","CIS"))

# # # Ex. 4
# name = "Nathalie"
# print(name.lower())
# print(name.upper())

# # # Ex. 5
# names = ["Nathalie" , "Nat" , "Nathe" , "Nathen", "Nate"]
# space = "#"
# print(space.join(names))

# Ex. 6

# name = "Nathalie"
# print(name.startswith("N"))

# # Ex. 7

# user_name = "nhimaya1"
# user_age = 21
# user_address = "1132 Drive"

# print(user_name.isalpha())
# print(str(user_age).isdigit())
# print(user_address.isalnum())

# # Ex. 9

# text=["No pain, no gain!?!"]
# punctuations = ['!', '?']

# for char in punctuations:
#     if char in text:
#         text = text.replace(char, '')

# print("Cleaned string:", text) 

## Ex. 10

# Given string
# text = "PythonPython"

# # Find the middle index
# middle_index = len(text) // 2

# # Split into two equal substrings
# first_half = text[:middle_index]
# second_half = text[middle_index:]

# # Display the substrings
# print("First half:", first_half)
# print("Second half:", second_half)

# # Ex. 11
# johnage = 21

# if johnage == 21:
#     print("True")
# else:
#     print("False") 

# # Ex. 12

# store_a_price = 400
# store_b_price = 530
# weight = 65  # in lbs
# shipping_rate = 1.25  # per pound

# store_a_total = store_a_price + (weight * shipping_rate)
# store_b_total = store_b_price  # free shipping

# print("Store A total: $", store_a_total)
# print("Store B total: $", store_b_total)

# if store_a_total < store_b_total:
#     print("Store A offers the better deal.")
# else:
#     print("Store B offers the better deal.")

## Ex. 13

# grades = [82, 91, 79, 63, 97]
# average = sum(grades) / len(grades)

# if average >= 90:
#     letter = "A"
# elif average >= 80:
#     letter = "B"
# elif average >= 70:
#     letter = "C"
# elif average >= 60:
#     letter = "D"
# else:
#     letter = "F"

# print("Average grade:", average)
# print("Letter grade:", letter)

## Ex. 14
# monthly_loss = [10, 12, 8, 5]

# total_loss = 0

# for loss in monthly_loss:
#     total_loss += loss

# print("Total weight lost over 4 months:", total_loss, "pounds")

# Ex. 15
# for num in range(0, 101, 2):
#     print(num)

# Ex. 16

# grades = [82, 91, 79, 63, 97]
# average = sum(grades) / len(grades)

# if average >= 90:
#     letter = "A"
# elif average >= 80:
#     letter = "B"
# elif average >= 70:
#     letter = "C"
# elif average >= 60:
#     letter = "D"
# else:
#     letter = "F"

# print("Average grade:", average)
# print("Letter grade:", letter)

# Ex. 25

# year1 = [200, 320, 180, 210, 175, 305]
# year2 = [550, 285, 195, 410]

# total1 = 0
# for amount in year1:
#     total1 += amount

# total2 = 0
# for amount in year2:
#     total2 += amount

# if total1 > total2:
#     print("Maria saved more in Year 1:", total1)
# else:
#     print("Maria saved more in Year 2:", total2)

# Ex. 24 

# nums = (10, 20, 30, 40)
# new_list = []

# for num in nums:
#     new_list.append(num + 10)

# print(new_list)

# # Ex. 23

# last_name = "Hernandez"
# children = ["Pablo", "Leila", "Jorge", "Karla", "Samuel"]

# for child in children:
#     print(child, last_name)

# Ex. 22

# # A
# student = {
#     "name": "John Doe",
#     "ID": 999999,
#     "Course": "CIS30A"
# }
# print(student)

# # B
# student["Semester"] = "Fall 2020"
# print(student)

# # C
# student["Course"] = "Python"
# print(student)

# # D
# del student["ID"]
# print(student)

# # E
# student.popitem()
# print(student)

# # F
# student.clear()
# print(student)

# # Ex 21
# t = (8, 11, 26, [32, 46])
# t[3][0] = 59
# t[3][1] = 66
# print(t)

# Ex 20 
# students = [['Jack', 'Lisa', 'Tomas', 'Daniel'], [22, 27, 30, 19]]

# # A
# for i in range(len(students[0])):
#     print(students[0][i], students[1][i])

# # B
# print(students[0][1], students[1][1])

# Ex 19
# animals = ['dogs', 'cats', 'birds']

# # A
# animals.append('rabbits')
# print(animals)

# # B
# animals.extend(['hamster', 'turtles', 'fishes'])
# print(animals)

# # C
# new_animals = animals + ['birds', 'snakes']
# print(new_animals)

# # D
# print(new_animals * 3)

# Ex 18

# nums = [100, 200, 300, 400, 500]

# for i in range(len(nums)):
#     nums[i] = nums[i] + i * 200

# print(nums)

# Ex 19
# # A
# for num in range(21):
#     if num == 11:
#         break
#     print(num)

# # B
# for num in range(26):
#     if num == 20:
#         continue
#     print(num)


cust_age = 75
if cust_age >= 65:
    print("You received senior discount!")
else:
    print("You cannot receive senior discount!")
