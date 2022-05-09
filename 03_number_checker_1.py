# Yes/No Checker function for checking validity of inputted numbers
def yes_no_checker(question):

    looping = True

    while looping:
        # Ask the user if they have played before
        user_response = input(question).strip().lower()

        # If user answers yes, game continues
        if user_response == "yes" or user_response == "y":
            user_response = "yes"
            return user_response

        # If the user answers no, display the instructions
        elif user_response == "no" or user_response == "n":
            user_response = "no"
            return user_response

        # If user answers anything other than yes or no
        else:
            print("<<<ERROR>>>\n<<<PLEASE ENTER YES OR NO>>>")


# Number Checker function for collecting how much the user would like to bet
def number_checker(question):

    looping = True

    while looping:

        try:
            # Ask the user how much they would like to bet
            bet_amount = int(input(question))

            # Check validity of input
            if 0 < bet_amount < 11:
                recheck_bet_amount = yes_no_checker(f"Are you sure you would like to bet ${bet_amount}? ")
                if recheck_bet_amount == "yes":
                    return bet_amount

            else:
                print("Please enter a number between 1 and 10.")

        # Check validity  of input 2
        except ValueError:
            print("Please enter a number between 1 and 10.")


# Main Routine
bet_counter = number_checker("How much money would you like to bet on your game? ")
print(f"You are betting ${bet_counter}")
