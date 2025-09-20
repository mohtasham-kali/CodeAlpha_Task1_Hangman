import random as r

def hangman_word():

    words = ["python", "code", "hangman", "game", "random"]
    word = r.choice(words)  # Randomly select a word
    attempts = 6  # Limit incorrect guesses

    print("Welcome to Word Hangman!")
    print("Try to guess the whole word. You have 6 attempts.\n")

    while attempts > 0:
        guess = input("Enter your word guess: ").lower()

        if guess == word:
            print("🎉 Congratulations! You guessed the word:", word)
            break
        else:
            attempts -= 1
            print(f"❌ Wrong guess! You have {attempts} attempts left.\n")

    if attempts == 0:
        print("💀 Game Over! The correct word was:", word)


hangman_word()
