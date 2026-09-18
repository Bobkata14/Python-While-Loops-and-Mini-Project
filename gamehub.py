# Game Hub

user = int()

secret_number = 7

attempts = 1
points = 0

while user != 4:
    print("===== GAME HUB =====\n")
    print("1. Play guess the number")
    print("2. Show game statistics")
    print("3. Add Points")
    print("4. Exit\n")
    user = int(input("Choose an option: "))

    print(" ")

    if user == 1:
        guess = int(input("Guess the number: "))

        while guess != secret_number:
            if guess > secret_number:
                print("Too high!")
                print()
            elif guess < secret_number:
                print("Too low!")
                print()

            guess = int(input("Guess the number: "))
            attempts += 1

        print("Correct!\n")
        points += 10

    if user == 2:
        print("====== statistics ======".upper())
        print(f"Attempts: {attempts}")
        print(f"Points: {points}")
        print("========================")
        print()

    if user == 3:
        points += int(input("Enter points to add: "))

        print(" ")
        print("Points added!")
        print(f"Current points: {points}")

    if user == 4:
        print("Thanks for playing!")
        print("Goodbye!")
        break


# Overall - 9.7/10