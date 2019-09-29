"""
File for getting the choices in the program
"""
_author_ = 'Jared Martinez'
_version_ = '09/29/2019'

# Dependencies
import random

# This Module gets the user's input
#
# Module user_choice()
#   Set string user_input = ''
#   Display 'Please pick an option:'
#   Display 'Rock'
#   Display 'Paper'
#   Display 'Scissors'
#   Input user_input
#   Set string user_input = user_input.lower()
#   return user_input
#  End Module
def user_choice():
    # Setting variable
    user_input = ''

    # Outputting options
    print('Please pick an option:')
    print('Rock')
    print('Paper')
    print('Scissors')

    # Getting input
    user_input = input('')
    user_input = user_input.lower()

    # Validating input
    return user_input;

# This module gets the computer's input
#
# Module computer_choice()
#   Set Array  computer_choices = ['Rock', 'Paper', 'Scissors']
#   Set integer computer_input = random integer (1, 3)
#   Set string computer_choice = computer_choices[computer_input]
#   return computer_choice
# End module

def computer_choice():
    computer_choices = ['rock', 'paper', 'scissors']
    computer_input = random.randint(0, 2)
    computer_choice = computer_choices[computer_input]
    return computer_choice