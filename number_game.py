# Import the random module

import random

# Generate a random secret number
def generate_secret_number():
    return random.randint(1, 100)

secret_number = generate_secret_number()
print(secret_number)


def play_game():
    # Ask the player for a guess
    secret_number = generate_secret_number()
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1

            if guess > secret_number:
                print("Too high! Try again.")
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid whole number.")
    