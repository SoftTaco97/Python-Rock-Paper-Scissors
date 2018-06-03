_author_ = 'Jared Martinez'

# This is a rock paper scissors simulator made in Python 3.6
# Based off of the user picking 1 for Rock, 2 for Paper, 3 for Scissors
# And a random number between 1 and 3 the program picks
# It then will compare the numbers and decide who wins.

# input list:
# user_input

# output list:
# user_result
# computer_result

# This Module gets the user's input
#
# Module user_choice()
#   Set integer user_input = 0
#   Display 'Please pick a number that corresponds with the item you wish to pick'
#   Display 'Rock [1] Paper [2] Scissors [3]'
#   Input user_input
#   return user_input
#  End Module

def user_choice():
    user_input = 0
    print('Please pick a number that corresponds with the item you wish to pick')
    print('Rock [1] Paper [2] Scissors [3]')
    user_input = int(input(''))
    return user_input

# This module gets the computer's input
#
# Module computer_choice()
#   Set integer computer_input = 0
#   import random
#   Set integer computer_input = random integer (1, 3)
#   return computer_input
# End module

def computer_choice():
    computer_input = 0
    import random
    computer_input = random.randint(1, 3)
    return computer_input

# This Function, compares the inputs and then decides the out come. After it has decided it
# Calls upon the appropriate module to display the results for the user.
#
# Function comparing_results(user_input, computer_input)
#   IF user_input == computer_input:
#       tie_message(user_input, computer_input)
#   ELIF user_input == 3 and computer_input == 1:
#       losing_message(user_input, computer_input)
#   ELIF user_input == 1 and computer_input == 3:
#       winning_message(user_input, computer_input)
#   ELIF user_input < computer_input:
#       losing_message(user_input, computer_input)
#   ELIF user_input > computer_input:
#       winning_message(user_input, computer_input)
#  End module

def comparing_results(user_input, computer_input):
    if user_input == computer_input:
        tie_message(user_input, computer_input)
    elif user_input == 1 and computer_input == 3:
        winning_message(user_input, computer_input)
    elif user_input == 3 and computer_input == 1:
        losing_message(user_input, computer_input)
    elif user_input < computer_input:
        losing_message(user_input, computer_input)
    elif user_input > computer_input:
        winning_message(user_input, computer_input)

# This function sets the String data user's results for the message modules
#
# Function setting_results_user(user_input)
#   Declare String user_result
#   IF user_input == 1:
#       Set String user_result = 'Rock'
#   ELIF user_input == 2:
#       Set String user_result = 'Paper'
#   ELIF user_input == 3:
#       Set String user_result = 'Scissors'
#   return user_result
# End module

def setting_results_user(user_input):
    user_result = ''
    if user_input == 1:
        user_result = 'Rock'
    elif user_input == 2:
        user_result = 'Paper'
    elif user_input == 3:
        user_result = 'Scissors'

    return user_result

# This Function sets the String data for the computer's results for the message modules
#
# Function setting_results_computer(computer_input)
#   Declare String computer_result = ''
#   IF computer_input == 1
#       Set String computer_result = 'Rock'
#   ELIF computer_input == 2
#       Set String computer_result = 'Paper'
#   ELIF computer_input == 3
#       Set String computer_result = 'Scissors'
#   return computer_result
# End module

def setting_results_computer(computer_input):
    computer_result = ''
    if computer_input == 1:
        computer_result = 'Rock'
    elif computer_input == 2:
        computer_result = 'Paper'
    elif computer_input == 3:
        computer_result = 'Scissors'
    return computer_result

# This module displays a message for the user if they have beaten the computer
#
# Module winning_message(user_input, computer_input)
#   Set computer_result = setting_results_computer(computer_input)
#   Set user_result = setting_results_user(user_input)
#   Display 'You picked', user_result, 'and the computer picked', computer_result, ', you win!'
# End module

def winning_message(user_input, computer_input):
    computer_result = setting_results_computer(computer_input)
    user_result = setting_results_user(user_input)
    print('You picked', user_result, 'and the computer picked', computer_result, ', you win!')

# This module displays a message for the user if they have tied the computer
#
# Module tie_message(user_input, computer_input)
#   Set user_result = comparing_results()
#   Set computer_result = comparing_results()
#   Display 'You picked', user_result, 'and the computer picked', computer_result, ', it's a tie!'
# End module

def tie_message(user_input ,computer_input):
    computer_result = setting_results_computer(computer_input)
    user_result = setting_results_user(user_input)
    print('You picked', user_result, 'and the computer picked', computer_result, ', its a draw!')

# This module displays a message for the user if they have lost to the computer
#
# Module losing_message(user_input, computer_input)
#   Set computer_result = setting_results_computer(computer_input)
#   Set computer_result = setting_results_user(user_input)
#   Display 'You picked', user_result, 'and the computer picked', computer_result, ', you lose!'
# End module

def losing_message(user_input, computer_input):
    computer_result = setting_results_computer(computer_input)
    user_result = setting_results_user(user_input)
    print('You picked', user_result, 'and the computer picked', computer_result, ', you lose!')

# Main Module
#
# Module main()
#   user_input = user_choice()
#   computer_input = computer_choice()
#   comparing_results(user_input,computer_input)
# End module

def main():
    user_input = user_choice()
    computer_input = computer_choice()
    comparing_results(user_input,computer_input)

# Calling the Main module
main()



