# Functions
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


# Main Routine
how_much = num_check("How many rounds would you like to pay? \n"
                     "The cost is $1 per round ", 0, 10)

print(f"You will be spending ${how_much}")
