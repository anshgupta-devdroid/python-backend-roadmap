first_number = float(input("Enter the first number : "))
second_number = float(input("Enter the second number : "))
total_number = first_number + second_number
subtraction_number = first_number - second_number
multiplication_number = first_number * second_number
division_number = first_number / second_number
floor_division_number = first_number // second_number
modulus_number = first_number % second_number
power_number = first_number ** second_number
print("===== ARITHMETIC OPERATORS =====")
print(f"First Number          : {first_number}")
print(f"Second Number         : {second_number}")
print(f"Sum                   : {total_number}")
print(f"Difference            : {subtraction_number}")
print(f"Product               : {multiplication_number}")
print(f"Quotient              : {division_number:.2f}")
print(f"Floor Quotient        : {floor_division_number}")
print(f"Remainder             : {modulus_number}")
print(f"Power                 : {power_number}")
print("===============================")