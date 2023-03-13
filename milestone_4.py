import random

class Hangman:
    def __init__(self, word_list: list, num_lives: int = 5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters: int = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses: list[str] = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')
        

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter")

            if guess.isalpha() == False:
                print('Invalid guess. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


