import random

# Word list with hints
words = {
    "python": "A coding language named after a snake, not a spaghetti monster.",
    "computer": "A machine that can do math, games, and stress your Wi-Fi.",
    "program": "A set of instructions that tells a computer what to do.",
    "developer": "Someone who turns coffee into code and bugs into features.",
    "keyboard": "The thing you smack when ideas appear faster than your typing.",
    "internet": "The giant web of cat videos, memes, and weird conspiracy theories.",
    "laptop": "A portable computer for working, gaming, and pretending to be productive."
}

# Select a random word and its hint
word, hint = random.choice(list(words.items()))

# Store letters guessed by the player
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 6

print("=" * 42)
print("        HANGMAN: CHAOS EDITION")
print("=" * 42)
print("Guess the word before the stickman starts judging you.")
print("You have 6 chances to embarrass yourself gracefully.")
print()

# Main game loop
while incorrect_guesses > 0:
    # Display the word with guessed letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("-" * 42)
    print("HINT BAR:", hint)
    print("-" * 42)
    print("Word:", display_word)
    print("Incorrect guesses left:", incorrect_guesses)

    # Check if the player has guessed the complete word
    if all(letter in guessed_letters for letter in word):
        print()
        print("🎉 You win! The word was:", word)
        print("You cracked it like a code wizard with extra coffee.")
        break

    # Get player's guess
    guess = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter. No full sentences, no chaos.")
        print()
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that one. The memory is strong, but the luck is weak.")
        print()
        continue

    # Add guess to the list
    guessed_letters.append(guess)

    # Check whether guess is correct
    if guess in word:
        print("✅ Correct! Nice one! You are basically a hangman genius.")
    else:
        incorrect_guesses -= 1
        print("❌ Wrong guess! That letter was a total flop.")

    print()

# If the player runs out of guesses
else:
    print()
    print("💀 Game Over! The stickman has officially won.")
    print("The correct word was:", word)
    print("Maybe next time your brain will do a better job than your typing.")

print()
print("=" * 42)
print("       THANKS FOR PLAYING! SEE YOU IN THE NEXT LEVEL!")
print("=" * 42)