looping = True

while looping:
    show_instructions = input("Have you played Lucky Unicorn before? ")

    if show_instructions == "yes":
        print("<<<CONTINUE TO GAME>>>")

    if show_instructions == "y":
        print("<<<CONTINUE TO GAME>>>")

    if show_instructions == "no":
        print("<<<INSTRUCTIONS>>>")

    if show_instructions == "n":
        print("<<<INSTRUCTIONS>>>")

    if show_instructions == "end":
        looping = False

    else:
        print("<<<ERROR>>>")
