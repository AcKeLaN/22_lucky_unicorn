# Lucky Unicorn Base Component

# Imports
import random
import time


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


# Press Enter function for token generator
def press_enter(question):

    looping = True

    while looping:
        # Ask the user if they have played before
        user_response = input(question).strip().lower()

        # If user answers yes, game continues
        if user_response == "":
            return user_response

        # If user answers anything other than yes or no
        else:
            print("Invalid Input\n"
                  "Please press enter to start your round ")


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
          "HAVE FUN!\n")


# Number Checker function for collecting how much the user would like to bet
def num_check(question, low, high):

    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # Ask the user the question
            response = int(input(question))

            # If the amount is too low / high, give feedback
            if low < response <= high:
                return response

            # Display an error
            else:
                print(error)

        except ValueError:
            print(error)


# Token Generator function for generating tokens
def token_generator():

    starting_balance = how_much
    balance = starting_balance
    round_counter = how_much

    valid = False

    while not valid:

        # Generate tokens
        start_round = press_enter("Press enter to start your round ")
        if start_round == "":
            time.sleep(3)
            chosen_num = random.randint(1, 100)
            round_counter -= 1

            # Adjust balance
            if 1 <= chosen_num <= 5:
                chosen = "unicorn"
                balance += 4
            elif 6 <= chosen_num <= 36:
                chosen = "donkey"
                balance -= 1
            else:
                if chosen_num % 2 == 0:
                    chosen = "horse"
                else:
                    chosen = "zebra"
                balance -= 0.5

            # Output
            print(f"You got a {chosen}!\n")

            # Looping
            if round_counter > 0:
                con = yes_no_checker("Would you like to continue? Y/N ").strip().lower()

                if con == "no" or con == "n":
                    valid = True

            if round_counter <= 0 or valid == True:
                print(f"---GAME OVER---\n"
                      f"Your final balance is ${balance}")
                break


# Main routine...
played_before = yes_no_checker("Have you played Lucky Unicorn before? ")
print(f"You chose {played_before}\n")

if played_before == "no":
    instructions()

how_much = num_check("How many rounds would you like to play? \n"
                     "The cost is $1 per round ", 0, 10)

print(f"You will be spending ${how_much}")

token_generator()
