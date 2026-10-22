import random

#different stages for hangman
stages=[
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]

max_mistakes=6


#Reading Words from file
def load_words():
    words=[]
    file=open("word.txt")
    for line in file:
        word=line.strip()
        if word.isalpha():
            words.append(word)
    file.close()
    return words


#for asking question
def get_guess(guessed_letters,wrong_letters):
    while True:
        guess=input("  Guess a letter: ").upper()
        if len(guess)!=1 or not guess.isalpha():
            print("\n  Please type one letter only!\n")
        elif guess in guessed_letters or guess in wrong_letters :
            print("\n  You have already used it!\n")
        else:
            return guess


#main game part
def game():
    words=load_words()
    secret_word=random.choice(words).upper()
    guessed_letters=set()
    wrong_letters=set()

    print("\n" + "=" * 32)
    print("         H A N G M A N")
    print("=" * 32)

    while True:
        display=make_display(secret_word,guessed_letters)
        wrong_text=" ".join(sorted(wrong_letters))

        print("\n" + "-" * 32)
        print(stages[len(wrong_letters)])
        print("\n  Word:    ", display)
        print("\n  Wrong:   ", wrong_text)
        print("\n  Mistakes:", len(wrong_letters), "/", max_mistakes)
        print("-" * 32 + "\n")

        #if the game reached at the end
        if "_" not in display:
            print("  *** YOU WIN!! ***\n")
            break
        if len(wrong_letters)==max_mistakes:
            print("  You lose! Better luck next time...")
            print("\n  The word was:", secret_word, "\n")
            break

        #checking every guess
        guess=get_guess(guessed_letters,wrong_letters)
        if guess in secret_word:
            print("\n  Good guess! ^_^")
            guessed_letters.add(guess)
        else:
            print("\n  Wrong! :-D")
            wrong_letters.add(guess)


#Showing the display
def make_display(secret_word,guessed_letters):
    display=""
    for letter in secret_word:
        if letter in guessed_letters:
            display=display + letter +" "
        else:
            display=display + "_ "
    return display

game()
