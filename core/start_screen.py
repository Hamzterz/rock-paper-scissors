"""
Rock, Paper, Scissors - Start Screen.

"""


def init():
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
            global INT_NUM_ROUNDS
            INT_NUM_ROUNDS = int(str_num_rounds)
            if (INT_NUM_ROUNDS % 2 == 1):
                bool_num_rounds_valid = True
            else:
                print("The inputted value for number of rounds was not valid. Please input an odd number.")
        except:
            print("Inputted value for number of rounds was not valid. Check if input is a valid number.")

    return INT_NUM_ROUNDS


def int_get_num_rounds():
    return INT_NUM_ROUNDS
