looping = True

while looping:
    show_instructions = input("Have you played Lucky Unicorn before? ").lower()

    if show_instructions == "yes":
        print("<<<CONTINUE TO GAME>>>")

    elif show_instructions == "y":
        print("<<<CONTINUE TO GAME>>>")

    elif show_instructions == "no":
        print("<<<INSTRUCTIONS>>>")

    elif show_instructions == "n":
        print("<<<INSTRUCTIONS>>>")

    else:
        print("<<<ERROR>>>")
