import random
from hangman_art import logo, stages
from hangman_words import word_list

lives = 6

chosen_word = random.choice(word_list)
print(logo)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"You have {lives}/6 lives left.")
    print(stages[lives])
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print("You've already guessed that letter.")


    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in my word. You lose a life. Try again if you dare...")

        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************\n my word was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

