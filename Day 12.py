import random
import art
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard'. ").strip().lower()
initial_guess = random.randint(1, 100)
if difficulty == "easy":
    total_attempts = 10
elif difficulty == "hard":
    total_attempts = 5

def number_guessing():
    global total_attempts
    while total_attempts != 0:
        print(f"You have {total_attempts} attempts to guess the number.")
        guess = int(input("Make a guess. "))
        if guess < initial_guess:
            total_attempts -= 1
            print("Too low.")
            print("Guess again.")
        elif guess > initial_guess:
            total_attempts -= 1
            print("Too high.")
            print("Guess again.")
        elif guess == initial_guess:
            print(f"You got it. The answer was {initial_guess}.")
            return
    print(f"You are out of guesses. The number was {initial_guess}.")
number_guessing()