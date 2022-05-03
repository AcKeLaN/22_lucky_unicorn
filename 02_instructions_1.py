# Yes/No checker function...
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


# Instructions function
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
            print("<<<CONTINUE TO GAME>>>")
