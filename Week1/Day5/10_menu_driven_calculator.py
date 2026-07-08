calculation_count = 0

while True:

    print("\n===== MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Thank you for using Calculator.")
        print(f"Total calculations: {calculation_count}")
        break

    elif choice >= 1 and choice <= 4:

        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", first_number + second_number)

        elif choice == 2:
            print("Result =", first_number - second_number)

        elif choice == 3:
            print("Result =", first_number * second_number)

        elif choice == 4:
            if second_number == 0:
                print("Cannot divide by zero.")
            else:
                print("Result =", first_number / second_number)

        calculation_count += 1

        again = input("Do you want another calculation? (yes/no): ").lower()

        if again == "no":
            print("Thank you for using Calculator.")
            print(f"Total calculations: {calculation_count}")
            break

    else:
        print("Invalid Choice")