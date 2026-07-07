age = 18
has_licence = "yes"
user_age = int(input("Enter your age: "))
user_has_licence = input("Do you have a driving licence? (yes/no): ")
print("You are eligible to drive.", user_age >= age and user_has_licence == has_licence)  

# age = 20
# has_license = True
# print(age >= 18 and has_license)
# print(age >= 18 or has_license)
# print(not has_license)