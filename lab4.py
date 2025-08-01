# # Ex. 1

# try:
#     age = int(input("Please enter a number 1-120: "))
#     assert 1 <= age <= 120 , "Age must be 1-120"
#     print("Valid Input")
# except ValueError: 
#     print("Thats not a valid number")
# except AssertionError as error:
#     print("Assertion Error", error)

# # assert age <= 1, print("Invalid Age, cannot be less than 1")

# # Ex. 2
# num = int(input("Input a number between 1-10: "))

# if 1 <= num <= 10:
#     print("Valid")
# else: 
#     raise Exception("Number is out of range")

# # Ex. 3

# try:
#     name = input("Enter your name: ")
#     assert name.isalpha(), "Name must contain only letters"
#     print("Hello", name)
# except AssertionError as error:
#     print("Assertion Error:", error)

# # Ex. 4

# try:
#     phone = input("Enter a 10-digit phone number: ")
#     assert phone.isdigit(), "Phone number must contain only digits"
#     assert len(phone) == 10, "Phone number must be exactly 10 digits long"
#     print("Good phone number")
# except AssertionError as error:
#     print("Assertion Error:", error)

# # Ex. 5

# class Student:
#     def __init__(self, name, ID, gender):
#         self.name = name
#         self.ID = ID
#         self.gender = gender
#         self.courses = []
    
#     def register(self):
#         print(self.name, " ", self.ID, " Student has been registered" )
        
#     def addCourse(self, courses):
#         self.courses.append(courses)
#         print(courses, " has been added to ", self.name, "'s course list" )

#     def greet(self):
#         print(f"Hello {self.name}!")

#     def printcourses(self):
#         print(f"{self.name}'s Courses: {', '.join(self.courses)}")

# student1 = Student("Nathalie", "83368", "Female")
# student2 = Student("Joash", "1028", "Male")

# student1.register()
# student2.register()

# student1.addCourse("Math")
# student1.addCourse("Science")
# student1.addCourse("CS")
# student2.addCourse("Math")
# student2.addCourse("EE")
# student2.addCourse("Discrete Structures")

# student1.greet()
# student2.greet()

# student1.printcourses()
# student2.printcourses()

# # Ex. 6

# class Vehicle:
#     def __init__(self, make, model, color, year, price):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.year = year
#         self.price = price

#     def display_description(self):
#         print(f"{self.year} {self.color} {self.make} {self.model} - ${self.price}")

# vehicle1 = Vehicle("Toyota", "Camry", "Blue", 2022, 27000)
# vehicle2 = Vehicle("Ford", "Mustang", "Red", 2023, 55000)

# vehicle1.display_description()
# vehicle2.display_description()

# # Ex. 10 
# class Person:
#     def __init__(self, name):
#         self.name = name

# class Employee(Person):
#     def __init__(self, name, emp_id):
#         super().__init__(name)
#         self.emp_id = emp_id

#     def display(self):
#         print("Name:", self.name)
#         print("Employee ID:", self.emp_id)

# emp = Employee("Nathalie", "E12345")
# emp.display()

# # Ex. 11
# class School:
#     def __init__(self, school_name):
#         self.school_name = school_name

# class Course(School):
#     def __init__(self, school_name, course_name):
#         super().__init__(school_name)
#         self.course_name = course_name

# class Room(Course):
#     def __init__(self, school_name, course_name, room_number):
#         super().__init__(school_name, course_name)
#         self.room_number = room_number

#     def display(self):
#         print(self.course_name)
#         print(f"Room {self.room_number}")
#         print(self.school_name)

# room_obj = Room("MVC", "Intro to Python", 16)
# room_obj.display()

my_list = [6, 2, 3, 9, 11, 4]
my_list.remove(2)
my_list.pop(2)
my_list.pop()
print(my_list)

