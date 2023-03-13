import random

word_list = ['banana', 'apple', 'grapes', 'strawberries', 'tomato']
word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again")
        return False

def ask_for_input():
    guess = input("Guess any letter: ")

    if guess.isalpha() == True and len(guess) == 1:
        check = check_guess(guess)
        if check == False:
            ask_for_input()
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        ask_for_input()

ask_for_input()
