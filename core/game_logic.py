"""
Rock, Paper, Scissors - Game Logic.

"""
import sys
import time
import random
from math import ceil
sys.path.append('./core')
from helpers.settings import DC_SELECTION_NAMES, DC_SELECTION_ART, Status


def init():
    bool_in_game = True

    while bool_in_game:
        print("Type 's', 'p', or 'r' to play.")
        str_user_selection = _str_get_valid_user_selection()
        _play_game(str_user_selection)
        bool_in_game = _bool_get_game_status()


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


def _str_get_cpu_selection():
    ls_selections = ['s', 'p', 'r']
    selection = random.choice(ls_selections)

    return selection


def _play_game(str_user_selection):
    str_cpu_selection = _str_get_cpu_selection()
    _in_game_dialogue(str_user_selection, str_cpu_selection)
    _get_winner(str_user_selection, str_cpu_selection)


def _in_game_dialogue(str_user_selection, str_cpu_selection):
    str_user_dialogue = DC_SELECTION_NAMES[str_user_selection]
    str_cpu_dialogue = DC_SELECTION_NAMES[str_cpu_selection]
    str_user_art = DC_SELECTION_ART[str_user_selection]
    str_cpu_art = DC_SELECTION_ART[str_cpu_selection]
    time.sleep(0.5)
    print('Rock...')
    time.sleep(0.5)
    print('Paper...')
    time.sleep(0.5)
    print('...Scissors!\n')
    time.sleep(0.5)
    print("USER: {}! \n {}".format(str_user_dialogue, str_user_art))
    print("CPU: {}. \n {}".format(str_cpu_dialogue, str_cpu_art))


def _get_winner(str_user_selection, str_cpu_selection):
    print("\nDecision:")
    if ((str_user_selection == 's') & (str_cpu_selection == 'p')) or ((str_user_selection == 'p') & (str_cpu_selection == 'r') or ((str_user_selection == 'r') & (str_cpu_selection == 's'))):
        print('User Wins!')
        Status.INT_USER_WINS += 1
    elif (str_user_selection == str_cpu_selection):
        print('Draw.')
    else:
        print('CPU Wins.')
        Status.INT_CPU_WINS += 1


def _bool_get_game_status():
    bool_game_on = True
    int_to_win = ceil(Status.INT_NUM_ROUNDS/2)
    print("---------------------------------------------------------------------------")
    print("SCORE:\nUser: {}\nCPU: {}".format(Status.INT_USER_WINS, Status.INT_CPU_WINS))
    print("Best of {}".format(Status.INT_NUM_ROUNDS))
    print("---------------------------------------------------------------------------\n")
    if Status.INT_USER_WINS == int_to_win:
        print('Game. Set. Match. You Win!')
        bool_game_on = False
    elif Status.INT_CPU_WINS == int_to_win:
        print('Game. Set. Match. You lose.')
        bool_game_on = False
    else:
        print("Next Round!")

    return bool_game_on


if __name__ == "__main__":
    init()
