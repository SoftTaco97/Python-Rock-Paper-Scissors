"""
Main Application file
"""
_author_ = 'Jared Martinez'
_version_ = '09/29/2019'

# Dependencies
import choices
import comparing
import messages
import validation

# Main Module
#
# Module main()
#   Set string user_input = choices.user_choice()
#   IF user_input is a valid choice
#       Set string computer_input = computer_choice()
#       Set string results = comparing_results.comparing_results(user_input,computer_input)
#       Display string results
#   ELSE
#       Display 'Not a valid option'
#       Call main()
# End module
def main():
    # Getting user input
    user_input = choices.user_choice()

    # Checking what we got back from the user
    if validation.validate_input(user_input):
        # Getting computer input
        computer_input = choices.computer_choice()

        # Getting the results
        results = comparing.comparing_results(user_input, computer_input)

        # Outputting the message
        messages.display_results(results)
    else:
        print('Not a valid choice! Try again.')
        main()
    

# Calling the main module
if __name__ == '__main__':
    main();