"""
File for comparing the choices selected in the program
"""
_author_ = 'Jared Martinez'
_version_ = '09/29/2019'

# This Module, compares the inputs and then decides the out come.
# 
#
# Module comparing_results(user_input, computer_input)
#   Set string message = ''
#   IF user_input == computer_input:
#       Set string message = 'tied!'
#   ELIF user_input == 'paper'
#       IF computer_input == 'rock'
#           Set string message = 'won!'
#       ElIF computer_input == 'scissors'
#           Set string message = 'lost!'
#   ELIF user_input == 'scissors'
#       IF computer_input == 'rock'
#           Set String message = 'lost!'
#       IF computer_input == 'paper'
#           Set String message = 'won!'
#   ELIF user_input == 'rock'
#       IF computer_input == 'paper'
#           Set String message = 'lost!'
#       ELIF computer_input == 'scissors'
#           Set String message = 'won!'
#   return 'You picked ' + user_input + ' and the computer picked ' + computer_input + ', you ' + message
# End module
def comparing_results(user_input, computer_input):
    message = ''
    if user_input == computer_input:
        message = 'tied!'
    elif user_input == 'paper':
        message = 'won!' if computer_input == 'rock' else 'lost!'
    elif user_input == 'scissors':
        message = 'won!' if computer_input == 'paper' else 'lost!'
    elif user_input == 'rock':
        message = 'won!' if computer_input == 'scissors' else 'lost!'
    return 'You picked ' + user_input + ' and the computer picked ' + computer_input + ', you ' + message