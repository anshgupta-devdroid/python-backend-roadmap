first_number = float(input("Enter the first number : "))
second_number = float(input("Enter the second number : "))
total = first_number + second_number
difference = first_number - second_number
product = first_number * second_number
quotient = first_number / second_number
floor_division_number = first_number // second_number
modulus_number = first_number % second_number
power_number = first_number ** second_number
print("===== ARITHMETIC OPERATORS =====")
print(f"First Number          : {first_number}")
print(f"Second Number         : {second_number}")
print(f"Sum                   : {total}")
print(f"Difference            : {difference}")
print(f"Product               : {product}")
print(f"Quotient              : {quotient:.2f}")
print(f"Floor Quotient        : {floor_division_number}")
print(f"Remainder             : {modulus_number}")
print(f"Power                 : {power_number}")
print("===============================")