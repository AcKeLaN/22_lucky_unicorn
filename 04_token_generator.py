from random import randint


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


def token_generator():

    looping = True

    while looping:
        give_token = yes_no_checker("Press enter to generate a token")
        if give_token == "yes":
            token = randint(1, 4)
            return token
