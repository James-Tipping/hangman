import random


word_list = ['banana', 'apple', 'grapes', 'strawberries', 'tomato']
word = random.choice(word_list)

# while True:
#     guess: str = input('Guess a letter')
#     if guess.isalpha():
#         if guess in word:
#             print(f'Good guess! {guess} is in the word.')
#             break
#         else:
#             print(f"Sorry, {guess} is not in the word. Try again")
#     else: 
#         print('Invalid letter. Please, enter a single alphabetical character')



def ask_for_input():
    while True:
        guess: str = input('Guess a letter')
        if guess.isalpha():
            check_guess(guess=guess)
            break
        else: 
            print('Invalid letter. Please, enter a single alphabetical character')

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')     
    else:
        print(f"Sorry, {guess} is not in the word. Try again")

check_guess()