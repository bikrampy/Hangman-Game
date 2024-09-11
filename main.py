# import random module
import random
from hangman_art import logo, stages
from hangman_word import word_list

# select a random word
random_word = random.choice(word_list)

random_word_list = []

empty_list = []

lives = 6

print(logo)

for letters in random_word:
    random_word_list.append(letters)  # convert the string into a list
    empty_list.append("_")

while lives > 0 and random_word_list != empty_list:

    empty_string = ""
    for characters in empty_list:
        empty_string += characters
    print(empty_string)

    guess_letter = input("Guess A Letter: ").lower()

    if guess_letter in empty_list:
        print("You already guessed the letter.")
        print(stages[lives])

    elif guess_letter in random_word:
        print("The letter is in the word.")
        print(stages[lives])
        for i in range(0, len(random_word_list)):
            if guess_letter == random_word_list[i]:
                empty_list[i] = guess_letter

    else:
        print("The letter is not in the word.")
        lives -= 1
        print(stages[lives])


if lives > 0:
    print("You win.")
else:
    print("You lost. Try again")
print(f"The word is {random_word}")
