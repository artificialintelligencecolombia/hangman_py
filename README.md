# Hangman Game

## Project Structure:

- hangman.py: The main script for running the game.
- words.py: A module for handling words and word-related operations.
- graphics.py: A module for managing hangman graphics.
- README.md: Documentation on how to play the game and the project's structure.

## Features:

1. Random Word Selection: Implement the choose_random_word() function in words.py to randomly select a word from a predefined list of words.
2. Input Validation: Implement a function in hangman.py to validate user input, ensuring it's a single letter and not guessed before.
3. Visual Representation of Hangman: 

- Implement a dictionary of ASCII art hangman stages in graphics.py.
- Create a function to retrieve the appropriate graphic for the current incorrect guesses.

4. Display Current State: Create a function to display the current state of the word being guessed. Undiscovered letters are displayed as underscores.

5. Win/Lose Conditions:

- Implement a function to check for win and lose conditions in hangman.py.
- Display messages for both winning and losing scenarios.

6. Play Again: After a game ends, offer the player the option to play again or exit the game.

## Code Organization:

1. hangman.py: 

- Import the necessary modules: random, words, and graphics.
- Implement the game loop that manages user input, word guessing, graphics, and win/lose conditions.
- Provide clear prompts for the user to guess a letter and display information about the game state.
- Offer an option to play again or exit the game loop.

2. words.py:

- Store a list of words for the game.
- Implement the choose_random_word() function to randomly select a word from the list.

3. graphics.py:

- Store the ASCII art graphics for different hangman stages as a dictionary.
- Implement a function to retrieve the appropriate graphic based on the current incorrect guesses.

## README.md:

Write a clear and comprehensive README.md that includes the following sections:

1. Introduction: Briefly introduce the Hangman game.

2. How to Play: Provide instructions on how to play the game, including how to guess letters and what happens on win/lose.

3. Project Structure: Explain the role of each script/module and how they collaborate.

4. Setup and Running: Guide users on how to run the game on their machine.

5. Features and Enhancements: List potential improvements or added features for future development.

6. Contributing: Encourage users to contribute and explain how they can do so.

7. License: Include licensing information.