"""Rock, Paper, Scissors Game - Python Learning

Make a rock-paper-scissors game where it is the player vs the computer. The
computer’s answer will be randomly generated, while the program will ask the
user for their input. This project will better your understanding of while
loops and if statements.

From https://www.codementor.io/@ilyaas97/6-python-projects-for-beginners-yn3va03fs

"""
from core import start_screen, game_logic


def main():
    start_screen.init()
    game_logic.init()


if __name__ == "__main__":
    main()
