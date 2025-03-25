import random

lowest_number = 1
highest_number = 100

answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a numer between {lowest_number} and {highest_number}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print("Number is out of range!")
            print(f"Please select a number between {lowest_number} and {highest_number}")
        elif guess < answer:
            print("Too low! Please try again")
        elif guess > answer:
            print("Too high! Please try again")
        else:
            print(f"CORRECT! The answer is {answer}")
            print(f"Your number of guesses was {guesses}")
            is_running = False


    else:
        print("Invalid guess!")
        print(f"Please select a number between {lowest_number} and {highest_number}")

    