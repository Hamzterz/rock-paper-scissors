"""
Settings for Rock, Paper, Scissors.

"""
import sys
sys.path.append('./core')
from lib.ascii_game_art import STR_ROCK_ART, STR_PAPER_ART, STR_SCISSORS_ART


class Status:
    INT_NUM_ROUNDS = 0
    INT_USER_WINS = 0
    INT_CPU_WINS = 0


DC_SELECTION_NAMES = {'s': 'Scissors', 'p': 'Paper', 'r': 'Rock'}
DC_SELECTION_ART = {'s': STR_SCISSORS_ART, 'p': STR_PAPER_ART, 'r': STR_ROCK_ART}
