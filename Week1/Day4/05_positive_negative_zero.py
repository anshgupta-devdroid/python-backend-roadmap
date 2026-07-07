user_number = int(input("Enter a number: "))
if user_number > 0:
    print("positive number")
    if user_number % 2 == 0:
        print("even number")
    else:
        print("odd number")    
elif user_number < 0:
    print("negative number")
else:
    print("zero")        