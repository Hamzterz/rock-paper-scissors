"""Rock, Paper, Scissors Game - Python Learning

Make a rock-paper-scissors game where it is the player vs the computer. The
computer’s answer will be randomly generated, while the program will ask the
user for their input. This project will better your understanding of while
loops and if statements.

From https://www.codementor.io/@ilyaas97/6-python-projects-for-beginners-yn3va03fs

"""


def _introduction_interaction():
    str_welcome_message = "Welcome to Rock, Paper, Scissors Game! Please input your name."
    print(str_welcome_message)
    str_username_input = input()
    str_successful_response = "Hi {}! How many rounds do you want to play for? (Please pick an odd number)".format(str_username_input)
    print(str_successful_response)
    int_num_rounds = _int_get_valid_num_rounds()
    print("Great. Best out of {}! Let's play!".format(int_num_rounds))


def _int_get_valid_num_rounds():
    bool_num_rounds_valid = False
    while bool_num_rounds_valid is False:
        str_num_rounds = input()
        try:
            int_num_rounds = int(str_num_rounds)
            if (int_num_rounds % 2 == 1):
                bool_num_rounds_valid = True
            else:
                print("The inputted value for number of rounds was not valid. Please input an odd number.")
        except:
            print("Inputted value for number of rounds was not valid. Check if input is a valid number.")


def _play_game():
    int_user_wins = 0
    int_cpu_wins = 0

    print("Type 's', 'p', or 'r' to play.")
    str_selection = _str_get_valid_user_selection()



def _str_get_valid_user_selection():
    bool_selection_valid = False
    while bool_selection_valid is False:
        ls_valid_selections = ['s', 'p', 'r']
        str_selection = input()
        if str_selection in ls_valid_selections:
            bool_selection_valid = True
        else:
            print("not a valid selection. Please try 's', 'p', or 'r'.")







def main():
    _introduction_interaction()
    _play_game()


if __name__ == "__main__":
    main()
