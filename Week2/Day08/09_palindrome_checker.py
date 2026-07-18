user = input("Enter any word : ")
reverse = user[::-1].lower()
if user.lower() == reverse:
    print(f"{user} is palindrome")
else:
    print(f"{user} is not palindrome")    