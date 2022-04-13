def yes_no_checker(question):

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


# Main routine...
looping = True

while looping:
    show_instructions = yes_no_checker("Have you played Lucky Unicorn before? ")
    print(f"You chose {show_instructions}")
