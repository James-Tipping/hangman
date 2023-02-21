import random

word_list = ['banana', 'apple', 'grapes', 'strawberries', 'tomato']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Choose any letter from the alphabet and type it in").lower()

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input")