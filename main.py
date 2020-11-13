from game import Hangman
from datetime import datetime


def intro():
    print("                  Welcome to HANGMAN!")
    print("The rules are simple, the computer will choose a word")
    print("and all you have to do is guess the right letters")
    print("Each missed letter counts as a part of the mans body")
    print("so choose your letters wisely or you will lose!")
    print("You can type 'save' at any time to save your progress")
    print()
    print()


def start_new():
    game = Hangman()
    game.new_word()
    return game


def load_save():
    pass


def check_guess(guess, game):
    '''Runs guess through Hangman class'''
    game.check_guess(guess)


def check_winner():
    pass


def print_game(game):
    print(game.print_board())
    print(game.get_correct())
    print(game.get_wrong())
    print(game.get_guessed())


def check_input(guess, game):
    '''Check if input is a single letter'''
    if guess == "exit":
        return guess

    if not guess.isalpha() or len(guess) > 1:
        return False

    elif guess in game.get_guessed():
        return False

    else:
        return True


def get_guess(game):
    '''Asks user for guess, checks input, returns guess'''
    while True:
        guess = input("Enter your guess: ")
        is_good = check_input(guess, game)

        if is_good:
            return guess
        else:
            print("Invalid input!")


def check_loser():
    pass


def main():
    intro()
    while True:
        guess = ""
        game = start_new()
        while guess.lower() != "exit":
            print_game(game)
            guess = get_guess(game)
            check_guess(guess, game)
            winner = check_winner()
            loser = check_loser()

            if winner or loser:
                break

        new_game = input("Would you like to play another game? [y/n]").lower()

        if new_game == "n":
            break
        elif new_game == "y":
            continue

main()
