import random

class Hangman:
    def __init__(self, word_list: list, num_lives: int = 5):
        self.word_list = ['banana', 'apple', 'grapes', 'strawberries', 'tomato']
        self.word: str = random.choice(self.word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters: int = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses: list[str] = []


