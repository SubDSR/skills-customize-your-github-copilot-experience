
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python that uses strings, loops, conditionals, and random selection. Players will guess letters to reveal a hidden word before they run out of attempts.

## 📝 Tasks

### 🛠️ Set Up the Word Game

#### Description
Create the core Hangman game structure, including the list of possible words, the randomly selected secret word, and the display for the player’s current progress.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Display the hidden word using underscore placeholders such as `_ _ _`
- Use Python strings and random selection to prepare the game state

### 🛠️ Handle Guesses and Game Endings

#### Description
Implement the guessing loop so the player can enter letters, track incorrect guesses, and see whether they win or lose.

#### Requirements
Completed program should:

- Accept letter guesses from the player
- Update the displayed progress when a correct letter is guessed
- Track incorrect guesses remaining
- End when the word is guessed or attempts are exhausted
- Display clear win and lose messages
