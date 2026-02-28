# Number Guessing Game Challenge

[Roadmap.sh Number Guessing Game Challenge](https://roadmap.sh/projects/number-guessing-game)

## Overview

This challenge is to implement a command-line number guessing game in Python. The game randomly selects a number between 1 and 100, and the player must guess the number within a limited number of attempts, based on the chosen difficulty level.

## How to Play

1. Run the game using Python:
   ```
   python main.py
   ```
2. You will be greeted with a welcome message and asked to choose a difficulty level:
   - **Easy**: 10 chances
   - **Medium**: 7 chances
   - **Hard**: 5 chances
3. Enter your guess for the number (between 1 and 100).
4. After each guess, you will be told if your guess is too high or too low.
5. The game continues until you guess the correct number or run out of chances.
6. At the end of each round, you will see:
   - Whether you won or lost
   - The correct number
   - How many chances you had left
   - The time you took to finish the game
7. You can choose to play again or exit.

## Features

- Difficulty selection with different number of chances
- Input validation for guesses
- Feedback after each guess (too high/too low)
- Replay option after each round
- Timer showing how long you took to finish

## Example Session

```
Welcome to the Number Guessing Game!
Guess a number between 1 and 100.
The number of chances you get is based on the difficulty level you choose.
Difficulty Levels:
1. Easy (10 chances)
2. Medium (7 chances)
3. Hard (5 chances)
Choose a difficulty level (1, 2, or 3): 2
You have chosen Medium level. You will get 7 chances to guess the number.
Enter your guess: 50
Too high! Try again.
You have 6 chances left.
Enter your guess: 25
Too low! Try again.
You have 5 chances left.
...
Congratulations! You've guessed the number 37 correctly!
You took 18.42 seconds to finish the game.
You had 3 chances left.
Do you want to play again? (y/n): n
Thank you for playing! Goodbye.
```

## Requirements

- Python 3.x
- No external dependencies
