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

# # Ex. 3
# thestring = 'I am a college student'
# print(thestring.replace("college","CIS"))

# # Ex. 4
# name = "Nathalie"
# print(name.lower())
# print(name.upper())

# # Ex. 5
# names = ["Nathalie" , "Nat" , "Nathe" , "Nathen", "Nate"]
# space = "#"
# print(space.join(names))

# # Ex. 6

# name = "Nathalie"
# print(name.startswith("N"))

# # Ex. 7

user_name = "nhimaya1"
user_age = 21
user_address = "1132 Drive"

print(user_name.isalpha())
# print(user_age.isdigit())
print(user_address.isalnum())