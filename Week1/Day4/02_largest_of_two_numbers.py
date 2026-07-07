first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))
if first_number > second_number:
    print(f"The largest number is : {first_number}")
elif first_number < second_number:
    print(f"The largest number is : {second_number}")
else:
    print("Both numbers are equal")        