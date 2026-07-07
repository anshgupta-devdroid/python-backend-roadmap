user_age = int(input("Enter your age: "))
if user_age < 0 or user_age > 120:
    print("Invalid age ")
elif user_age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")        