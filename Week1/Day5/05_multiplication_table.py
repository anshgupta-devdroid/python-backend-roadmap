user_number = int(input("Enter any number : "))
i = 1
if user_number <= 0:
    print("Invalid number")
else:    
  while i <= 10:
    print(f"{user_number} x {i} = {user_number * i}")
    i += 1