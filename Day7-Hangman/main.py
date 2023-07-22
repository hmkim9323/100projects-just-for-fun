#Step 1

word_list = ["aardvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

end_of_game = False
# make a new list displaying the blanks
display = []
for letter in chosen_word:
    display += "_"

deathMomemt = 6
lifeCount = 0

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    checkFlag = False
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            ceckFlag = True
            print(display)

    if checkFlag == False:
        lifeCount += 1

    if lifeCount == deathMomemt:
        print("You lose.")
        end_of_game = True

    if "_" not in display:
        end_of_game = True
        print("You win.")
        end_of_game = True


