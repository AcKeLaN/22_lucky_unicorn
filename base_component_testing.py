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


# Instructions function for displaying instructions when called
def instructions():
    print("INSTRUCTIONS:\n"
          "You must pay an amount of money (up to $10.00) to start the game.\n"
          "Each round costs $1.00.\n"
          "Press 'enter' to start your round.\n"
          "A token will be generated for you for each round that you play.\n"
          "This can either be a Unicorn, Horse, Zebra, or Donkey.\n"
          "If you get a Unicorn you win $5.00.\n"
          "if you get a Zebra or Horse you win 50c.\n"
          "if you get a Donkey you win nothing.\n"
          "You can choose to stop playing after any round.\n"
          "HAVE FUN!")


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


# Main routine...
played_before = yes_no_checker("Have you played Lucky Unicorn before? ")
print(f"You chose {played_before}")

if played_before == "no":
    show_instructions = yes_no_checker("Would you like to see the instructions? ")
    print(f"You chose {show_instructions}")
    if show_instructions == "yes" or show_instructions == "y":
        instructions()
    elif show_instructions == "no" or show_instructions == "n":
        recheck_show_instructions = yes_no_checker("Are you sure? Would you like to see the instructions? ")
        if recheck_show_instructions == "yes" or recheck_show_instructions == "y":
            instructions()
        else:
            bet_counter = number_checker("How much money would you like to bet on your game? ")
            print(f"You are betting ${bet_counter}")

bet_counter = number_checker("How much money would you like to bet on your game? ")
print(f"You are betting ${bet_counter}")
