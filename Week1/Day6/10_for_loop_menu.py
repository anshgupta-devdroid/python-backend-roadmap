while True:

    print("\n==== MENU ====")
    print("1. Print Numbers 1-10")
    print("2. Multiplication Table")
    print("3. Print Even Numbers")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Thank You!")
        break

    elif choice == 1:
        for i in range(1, 11):
            print(i)

    elif choice == 2:
        n = int(input("Enter any number: "))

        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")

    elif choice == 3:
        for i in range(2, 21, 2):
            print(i)

    else:
        print("Invalid Choice")