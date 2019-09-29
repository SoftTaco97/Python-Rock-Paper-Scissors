"""
File for validating user inputs
"""
_author_ = 'Jared Martinez'
_version_ = '09/29/2019'

# This module validates user input
#
# Module validate_input(user_input)
#   Set Array choices = ['rock', 'paper', 'scissors']
#   IF user_input is in the choices array
#       return TRUE
#   ELSE
#       return FALSE
# End module
def validate_input(user_input):
    choices = ['rock', 'paper', 'scissors']
    return user_input in choices