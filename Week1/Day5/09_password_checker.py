# password = "python123"
# attempt = 3 
# while True :
#     user_password = input("Enter your password : ")
#     attempt -= 1

#     if user_password == password:
#         print("Login successfull")
#         print(f"Attempt left : {attempt}")
#         break 
        

#     else :
#         print("Wrong password")
#         print(f"Attempt left : {attempt}")
        
#         if attempt == 0:
#             print("Account Locked")
#             break;

      
    
correct_password = "python123"
attempts_used = 0
max_attempts = 3

while attempts_used < max_attempts:
    user_password = input("Enter your password: ")
    attempts_used += 1

    if user_password == correct_password:
        print("Login Successful!")
        print(f"Attempts used: {attempts_used}")
        break

    else:
        attempts_left = max_attempts - attempts_used
        print("Wrong Password!")

        if attempts_left > 0:
            print(f"Attempts left: {attempts_left}")
        else:
            print("Account Locked!")

else:
    print("Access Denied.")


