# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1

- The environment was setup on GitHub for this project. 

- The GitHub repository allows for easy upload and review of code by AICore's automated systems.

![image of repository](./Screenshot%202023-02-22%20at%2002.27.03.png)

## Milestone 2

- In this milestone, a list of words was created, a random choice from the list was made, and the choce was printed out

```python
import random

word_list = ['banana', 'apple', 'grapes', 'strawberries', 'tomato']
print(word_list)

word = random.choice(word_list)
print(word)
```

Then the user is asked to input a letter. If the character entered is not a letter, the user is told to enter a valid input

```python
guess = input("Choose any letter from the alphabet and type it in")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input")
```

![image of program output](Screenshot%202023-03-10%20at%2017.59.11.png)

## Milestone 3

- In this milestone, two functions were created to take in an input from the user.
- If the letter is not in the alphabet, the user is prompted to try again
- If the letter is in the word, the program exits. Otherwise, the user is prompted to try again


![image of program input](/Screenshot%202023-03-13%20at%2022.01.38.png)

