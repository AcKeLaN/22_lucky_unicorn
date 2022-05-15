from random import randint
from time import sleep


# Yes/No checker function for various validity checks
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
            print("Invalid Input\n"
                  "Please enter either 'yes' or 'no'.")


# Press Enter function to ask the user to press enter to start the game
def press_enter(question):

    looping = True

    while looping:
        # Ask the user to press enter to start the game
        user_response = input(question).strip().lower()

        # If user presses enter, game continues
        if user_response == "":
            user_response = ""
            return user_response

        # If user presses something other than enter
        else:
            print("Invalid Input")


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


# Token Generator function that generates a token
def token_generator(bet_counter=None):

    looping = True

    while looping:
        while total_money > 0:
            give_token = press_enter("Press enter to start the game... ")
            if give_token == "":
                sleep(3)
                token = randint(1, 10)

                if 1 <= token <= 5:
                    print("You got a Donkey!")
                    print("You have won $0.00!")
                    total_money = total_money - 1
                    print(f"You have ${total_money} left.")

                elif 6 <= token <= 7:
                    print("You got a Horse!")
                    print("You have won 50 cents!")
                    total_money = total_money - 0.5
                    print(f"You have ${total_money} left.")

                elif 8 <= token <= 9:
                    print("You got a Zebra!")
                    print("You have won 50 cents!")
                    total_money = total_money - 0.5
                    print(f"You have ${bet_counter} left.")

                elif token == 10:
                    print("You got a Unicorn!")
                    print("You have won $5.00!")
                    total_money = total_money + 4
                    print(f"You have ${total_money} left.")


# Main Routine
total_money = number_checker("How much money would you like to bet on your game? ")
print(f"You are betting ${total_money}")
