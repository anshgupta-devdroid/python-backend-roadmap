correct_password = "python123"

for attempt in range(1, 4):

    user_password = input("Enter your password: ")

    if user_password == correct_password:
        print("Login Successful!")
        print(f"Attempts used: {attempt}")
        break

    elif attempt == 3:
        print("Account Locked!")

    else:
        print("Wrong Password!")
        print(f"Attempts left: {3 - attempt}")