import random


word_list = ['banana', 'apple', 'grapes', 'strawberries', 'tomato']
word = random.choice(word_list)

while True:
    guess: str = input('Guess a letter')
    if guess.isalpha():
        if guess in word:
            print(f'Good guess! {guess} is in the word.')
            break
        else:
            print(f"Sorry, {guess} is not in the word. Try again")
    else: 
        print('Invalid letter. Please, enter a single alphabetical character')