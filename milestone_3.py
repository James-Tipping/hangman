

while True:
    guess: str = input('Guess a letter')
    if guess.isalpha():
        break
    else: 
        print('Invalid letter. Please, enter a single alphabetical character')