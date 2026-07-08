secret_number = 7
attempt = 0

while True:
    user_number = int(input("Guess the number: "))
    attempt += 1

    if user_number == secret_number:
        print("Correct! You guessed the secret number.")
        print(f"Attempts: {attempt}")
        break

    elif user_number > secret_number:
        print("Too high!")

    else:
        print("Too low!")