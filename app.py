import random

def play_game():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    attempts = 0

    # Welcome message and ask for the user's name
    print("Welcome to the Number Guessing Game!")
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

    # Game rules
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess the number.")

    while attempts < 10:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"Congratulations, {name}! You guessed the number {number} correctly in {attempts} attempts.")
            break

    if guess != number:
        print(f"Game over, {name}! You couldn't guess the number {number} within 10 attempts.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thank you for playing the Number Guessing Game. Goodbye!")

# Start the game
play_game()
