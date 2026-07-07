username = "admin"
password = "password123"

input_username = input("Enter username: ")
input_password = input("Enter password: ")

if input_username == username and input_password == password:
    print("Login successful!")
elif input_username == username and input_password != password:
    print("Wrong password.")
elif input_username != username and input_password == password:
    print("Wrong username.")    
else:
    print("Invalid username or password.")