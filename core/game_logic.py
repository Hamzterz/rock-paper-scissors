"""
Rock, Paper, Scissors - Game Logic.

"""
import time
import random
from lib.ascii_game_art import STR_ROCK_ART, STR_PAPER_ART, STR_SCISSORS_ART

DC_SELECTION_NAMES = {'s': 'Scissors', 'p': 'Paper', 'r': 'Rock'}


def init():
    int_user_wins = 0
    int_cpu_wins = 0
    bool_in_game = True

    while bool_in_game:
        print("Type 's', 'p', or 'r' to play.")
        str_user_selection = _str_get_valid_user_selection()
        _play_game(str_user_selection)


def _str_get_valid_user_selection():
    bool_selection_valid = False
    while bool_selection_valid is False:
        ls_valid_selections = ['s', 'p', 'r']
        str_user_selection = input()
        if str_user_selection in ls_valid_selections:
            bool_selection_valid = True
        else:
            print("not a valid selection. Please try 's', 'p', or 'r'.")

    return str_user_selection


def _play_game(str_user_selection):
    str_cpu_selection = _str_get_cpu_selection()
    _in_game_dialogue()
    print(DC_SELECTION_NAMES[str_user_selection])
    print(DC_SELECTION_NAMES[str_cpu_selection])


def _in_game_dialogue():
    time.sleep(0.5)
    print('Rock...')
    time.sleep(0.5)
    print('Paper...')
    time.sleep(0.5)
    print('...Scissors!')


def _user_vs_cpu_selection(str_user_selection, str_cpu_selection):
    print('x')


def _str_get_cpu_selection():
    ls_selections = ['s', 'p', 'r']
    selection = random.choice(ls_selections)

    return selection


if __name__ == "__main__":
    #print(_str_get_cpu_selection())
    #init()
    print(STR_ROCK_ART)
    print(STR_PAPER_ART)
    print(STR_SCISSORS_ART)
