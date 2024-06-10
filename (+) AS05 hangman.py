import random

wordlist = ["apple", "banana", "orange", "grape", "pear", "pineapple", "strawberry", "watermelon", "kiwi", "blueberry","papaya"]

def choose_word():
    return random.choice(wordlist)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    print("Hangman - Start")
    word = choose_word()
    guessed_letters = []
    attempts = 7
    
    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)
        
        if "_" not in display_word(word, guessed_letters):
            print("Correct. You guessed the word:", word)
            break
        
        if attempts == 0:
            print("Out of attempts. The word was:", word)
            break
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word:
            attempts -= 1
            print("Incorrect guess!")
        
if __name__ == "__main__":
    hangman()
