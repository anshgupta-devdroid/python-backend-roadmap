user_number = int(input("Enter any positive number : "))
i = 1
total = 0
if user_number <= 0:
          print("Invalid Number")
else:          
  while i <= user_number:
     total += i
     i += 1
  print(f"Sum of all natural number :{sum} ")     