import random
import time

max = 100
min = 1


def generate_random_number():
    return random.randint(min, max)


def main():
    while True:
        print("Welcome to the Number Guessing Game!")
        print(f"Guess a number between {min} and {max}.")
        print(
            "The number of chances you get is based on the difficulty level you choose."
        )
        print("Difficulty Levels:")
        print("1. Easy (10 chances)")
        print("2. Medium (7 chances)")
        print("3. Hard (5 chances)")
        difficulty = input("Choose a difficulty level (1, 2, or 3): ")
        if difficulty == "1":
            print(
                "You have chosen Easy level. You will get 10 chances to guess the number."
            )
            chances = 10
        elif difficulty == "2":
            print(
                "You have chosen Medium level. You will get 7 chances to guess the number."
            )
            chances = 7
        elif difficulty == "3":
            print(
                "You have chosen Hard level. You will get 5 chances to guess the number."
            )
            chances = 5
        else:
            print("Invalid choice. Defaulting to Easy level.")
            chances = 10

        random_number = generate_random_number()
        start_time = time.time()
        while chances > 0:
            guess = input("Enter your guess: ")
            if not guess.isdigit():
                print("Please enter a valid number.")
                continue
            guess = int(guess)
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                end_time = time.time()
                elapsed = end_time - start_time
                print(
                    f"Congratulations! You've guessed the number {random_number} correctly!"
                )
                print(f"You took {elapsed:.2f} seconds to finish the game.")
                print(f"You had {chances} chances left.")
                break
            chances -= 1
            print(f"You have {chances} chances left.")
        else:
            end_time = time.time()
            elapsed = end_time - start_time
            print(f"Game Over! The correct number was {random_number}.")
            print(f"You took {elapsed:.2f} seconds to finish the game.")
        replay = input("Do you want to play again? (y/n): ").strip().lower()
        if replay != "y":
            print("Thank you for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
