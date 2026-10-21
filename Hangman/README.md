# Hangman

A simple command-line Hangman game written in Python.

A random word is picked from a text file. Guess it one letter at a time before you run out of mistakes.

## Features

- Secret word chosen at random from `word.txt` with `random.choice()`
- Correct letters are tracked in a set and shown as a masked word, e.g. `_ A _ L O A D`
- 6 mistakes allowed, with ASCII gallows art that grows with each wrong guess
- Rejects invalid input (more than one character, digits, symbols) and repeated letters without counting them as mistakes
- Input is case-insensitive

## Requirements

- Python 3.6 or newer
- No external libraries

## Setup

1. Put `hangman.py` and `word.txt` in the same folder.
2. Add your words to `word.txt`, one word per line, letters only:

```
python
socket
kernel
firewall
```

Lines that are blank or contain spaces, digits or symbols are ignored.

## How to run

Open a terminal in the project folder and run:

```
python hangman.py
```

## How to play

1. The game shows the gallows, the masked word and your wrong letters.
2. Type one letter and press Enter.
3. A correct letter is revealed in the word. A wrong letter adds a body part to the gallows.
4. You win when every letter is revealed. You lose after 6 wrong guesses, and the word is shown.

## Example

```
  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Word: _ A Y _ O A D
Wrong letters: {'Z', 'Q'} ( 2 / 6 )
Guess A Letter:
```

## Code structure

| Function | What it does |
|---|---|
| `load_words()` | Reads `word.txt` and returns a list of valid words |
| `get_guess()` | Asks until the player enters one new letter, then returns it |
| `make_display()` | Builds the masked word from the correct guesses |
| `game()` | Runs the full game loop |

Settings:

- `max_mistakes` — number of wrong guesses allowed (default `6`). If you change it, add matching entries to `stages`.
- `stages` — list of ASCII pictures, one per mistake count.

## Files

```
hangman.py   the game
word.txt     the word list
README.md    this file
```