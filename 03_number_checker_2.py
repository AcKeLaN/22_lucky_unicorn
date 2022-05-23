# Functions

# Main Routine

error = "Please enter a whole number between 1 and 10\n"

valid = False
while not valid:
    try:
        # Ask the user the question
        response = int(input("How many rounds would you like to pay? \n"
                             "The cost is $1 per round "))

        # If the amount is too low / high, give feedback
        if 0 < response <= 10:
            print(f"You have asked to play with ${response} ")
            valid = True

        # Display an error
        else:
            print(error)

    except ValueError:
        print(error)
