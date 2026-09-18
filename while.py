# Python While

"""
Python Loops
Python has two primitive loop commands:

while loops
for loops
"""

"""
The while Loop
With the while loop we can execute a set of statements as long as a condition is true."""

# Print i as long as i is less than 6:
i = 1
while i < 6:
    print(i)
    i += 1

#Note: remember to increment i, or else the loop will continue forever.

"""
The while loop requires relevant variables to be ready, in this example
we need to define an indexing variable, i, which we set to 1.
"""

"""
The break Statement
With the break statement we can stop the loop even if the while condition is true:"""

# Exit the loop when i is 3:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

"""
The continue Statement
With the continue statement we can stop the current iteration, and continue with the next:"""

#Continue to the next iteration if i is 3:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


"""
The else Statement
With the else statement we can run a block of code once when the condition no longer is true:"""

# Print a message once the condition is false:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# Note: The else block will NOT be executed if the loop is stopped by a break statement.


"""
Code Challenge:

Create a variable i with the value 0
Write a while loop that runs as long as i is less than 6
Inside the loop: increment i by 1
If i equals 3, use continue to skip that iteration
Print i"""

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# Exercise 1
i = 0
while i < 10:
    i += 1
    print(i)


# Exercise 2
i = 11
while i > 1:
    i -= 1
    print(i)


# Exercise 3
i = 0
while i < 20:
    i += 2
    print(i)


# Exercise 4
number = 1
total = 0

while number <= 100:
    total += number
    number += 1

print(total)


# Exercise 5
password = "python123"

user_input = input("Enter your password: ")

while user_input != password:
    print("Access Denied!")
    print()
    user_input = input("Enter your password: ")

print("Access Granted")


# Exercise 6
number = 0

user_input = int(input("Enter a number: "))

while user_input != number:
    user_input = int(input("Enter a number: "))

print("Program finished")


# Exercise 7

total_sum = 0
number = int(input("Enter a number: "))

while number != 0:
    total_sum += number
    number = int(input("Enter a number: "))

print()
print(f"Total: {total_sum}")


# Exercise 8

secret_number = 7

user = int(input("Guess: "))

while user != secret_number:
    if user > secret_number:
        print("Too high")
        user = int(input("Guess: "))
    elif user < secret_number:
        print("Too low")
        user = int(input("Guess: "))

print("Correct!")

#Exercise 9

balance = 1000
choice = ""

while choice != "4":
    print("====ATM====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choice an option: ")
    print()

    if choice == "1":
        print(f"Balance: {balance}")
        print()

    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print(f"Successfully deposited {amount} to {balance}")
        print()

    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        if amount < balance:
            balance -= amount
            print(f"Successfully withdrew {amount}")
        else:
            print("Insufficient balance!")
        print()

    elif choice == "4":
        print("Goodbye!")

    else:
        print("Invalid option! Please choice between 1 and 4")
        print()


# Exercise 10
total_numbers = 0
total_sum = 0
positive_count = 0
negative_count = 0

number = int(input())

while number != 0:
    total_numbers += 1
    total_sum += number

    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1

    number = int(input())

print()
print(f"Total numbers: {total_numbers}")
print(f"Sum: {total_sum}")
print(f"Positive numbers: {positive_count}")
print(f"Negative numbers: {negative_count}")


#Overall - 9.7/10