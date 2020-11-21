import random
from hangman_art import logo, stages
from hangman_words import word_list


chosen_word = random.choice(word_list)
chosen_word_len = len(chosen_word)
display = ["_"] * chosen_word_len
print("Psst, the solution is {}".format(chosen_word))

lives = 6
end_of_game = False
print(logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    guessed = False
    if guess in display:
        print("You have already guessed {}".format(guess))
        print("".join(display))
        continue
    for pos in range(chosen_word_len):
        if guess == chosen_word[pos]:
            display[pos] = guess
            guessed = True

    if not guessed:
        print("You guessed {}, that's not in the word. You lose a life.".format(guess))
        lives = lives - 1
        if lives == 0:
            print("You lose.")
            end_of_game = True
    else:
        print("".join(display))

    if "_" not in display:
        print("You win!")
        end_of_game = True
    
    print(stages[lives])
    print("-------------------")