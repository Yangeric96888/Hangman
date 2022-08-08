import random
import re


def initalize_game():
    try_left = 8
    word_list = ["python", "eric", "java", "github"]
    current_word = random.choice(word_list)
    current_letter = ""
    guess_hint = len(current_word) * "-"
    already_guessed = set()

    return (try_left, word_list, current_word, current_letter, guess_hint, already_guessed)


def is_letter_valid(current_letter, already_guessed) -> bool:
    if len(current_letter) != 1:
        print("Your guess must be 1 letter please!")
        return False
    elif current_letter.isupper():
        print("Your guess must be lowercase please!")
        return False
    elif current_letter in already_guessed:
        print("You already guessed this letter!")
        return False
    else:
        return True


def is_letter_in_word(current_word, current_letter):
    if current_letter in current_word:
        return True
    return False


# Runs when letter is correct
def right_letter(current_word, current_letter, guess_hint, already_guessed):
    index_of_occurrence = [m.start() for m in re.finditer(current_letter, current_word)]
    for index in index_of_occurrence:
        guess_hint = guess_hint[:index] + current_letter + guess_hint[index + 1:]
        print(guess_hint[index])
    already_guessed.add(current_letter)

    return guess_hint


# Runs when letter is wrong
def wrong_letter(current_letter, already_guessed):
    already_guessed.add(current_letter)
    print("Not in the word!")

def is_win(current_word, guess_hint):
    if current_word == guess_hint:
        print("You wonnnn!")
        print("\n")
        return True
    else:
        return False


def turn(try_left, current_word, guess_hint, already_guessed) -> str:
    print("\n")
    game_status = "continue"
    print(guess_hint)
    current_letter = input("Guess a letter: ")

    # Forces player to submit valid letter
    while not is_letter_valid(current_letter, already_guessed):
        current_letter = input("Guess another letter: ")

    # Checks if letter is successful or not
    if is_letter_in_word(current_word, current_letter):
        guess_hint = right_letter(current_word, current_letter, guess_hint, already_guessed)
        if is_win(current_word, guess_hint):
            game_status = "win"
            return [guess_hint, game_status, try_left]
    else:
        wrong_letter(current_letter, already_guessed)
        try_left -= 1

    return [guess_hint, game_status, try_left]


def game() -> str:
    try_left, word_list, current_word, current_letter, guess_hint, already_guessed = initalize_game()
    game_status = ""

    while try_left > 0:
        guess_hint, game_status, try_left = turn(try_left, current_word, guess_hint, already_guessed)
        if game_status == "win":
            return "win"
    else:
        print("You lost, sorry!")
        print("\n")
        return "loss"
