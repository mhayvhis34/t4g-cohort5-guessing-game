# Import the random module

import random

# Generate a random secret number
def generate_secret_number():
    return random.randint(1, 100)

secret_number = generate_secret_number()
print(secret_number)

    