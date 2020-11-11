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
    return game


def load_save():
    pass


def check_guess():
    pass


def check_winner():
    pass


def print_game():
    pass


def check_input():
    pass


def get_guess():
    pass


def check_loser():
    pass


def main():
    intro()
    while True:
        guess = ""
        game = start_new()
        while guess.lower() != "exit":
            print_game()
            guess = get_guess()
            check_guess(guess)
            winner = check_winner(game.get_word_length())
            loser = check_loser()
            if winner:
                declare_winner()
                break
            if loser:
                declare_loser()
                break
        continue = input("Would you like to play another game? [y/n]").lower()
        if continue == "n":
            break



