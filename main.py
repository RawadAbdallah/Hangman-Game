import random
import os
from art import gameover, hangman_txt, hangman, won
from wordlist import word_list


def console_clear():
    os.system('clear')


print(hangman_txt)
print("\t\tPress 'Enter' to play")
input()
console_clear()

#Choosing a random word from the word list
word = word_list[random.randint(0, len(word_list) - 1)]
blank = ""
temp = word
hint = [word[0], word[random.randint(1, len(word) - 2)], word[len(word) - 1]]
hints = (int)(len(word) / 2) - 1
#filling the blanks with '_'
for i in word:
    blank += "_"
print(
    "The word is : " + blank +
    "\t\t type !hint to show one letter\nHints Remaining :", hints)
print(hangman[0])
lives = 6
found = False
art = 0
while lives > 0:
    guess = input("Enter your guess: ")

    i = 0

    # comparing the guess of the player with the word
    while i < (len(word)):
        if hints > 0:
            if guess == "!hint" or guess == " !hint" or guess == " !hint " or guess == "!hint ":
                guess = hint[hints - 1]
                hints -= 1

        if guess == word[i]:
            blank = blank[:i] + guess + blank[i + 1:]
            word = word[:i] + "_" + word[i + 1:]
            found = True

        if blank == temp:
            break

        i += 1
    if not found:
        art += 1
        lives -= 1
#clearing the console
    console_clear()

    print(
        "The word is : " + blank +
        "\t\t type !hint to show one letter\nHints Remaining :", hints)
    print(hangman[art])
    print("Lives = ", lives)
    found = False
    if blank == temp:
        break

if lives == 0:
    console_clear()
    print(gameover)
    print("The correct word was :" + temp)
else:
    console_clear()
    print(won)
    print('\t\t\t' + temp)
    print('🏆 You have found the correct word. 🏆')
