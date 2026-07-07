user = int(input("Enter a year:"))
if user <= 0:
    print("Invalid year")
else:
    if (user % 4 == 0 and user % 100 != 0) or (user % 400 == 0):
        print(f"{user} is a leap year")
    else:
        print(f"{user} is not a leap year")        