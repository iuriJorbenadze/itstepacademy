
import random

def number_guessing_game(interval_start, interval_end, lives):
    # Randomly choosing a number within the given interval
    secret_number = random.randint(interval_start, interval_end)

    print(f"Guess the number between {interval_start} and {interval_end}. You have {lives} lives.")

    while lives > 0:
        try:
            guess = int(input("Enter your guess: "))
            if guess == secret_number:
                print("Congratulations! You guessed the number!")
                return
            elif guess < secret_number:
                print("The number is higher.")
            else:
                print("The number is lower.")
            lives -= 1
            print(f"Lives remaining: {lives}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print(f"Game over! The number was {secret_number}.")

# Example usage
# number_guessing_game(1, 100, 5)  # Uncomment this line to test the game
