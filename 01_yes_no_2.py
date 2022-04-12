looping = True

while looping:
    show_instructions = input("Have you played Lucky Unicorn before? ").strip().lower()
    if show_instructions == "yes" or show_instructions == "y":
        print("<<<CONTINUE TO GAME>>>")
    elif show_instructions == "no" or show_instructions == "n":
        print("<<<INSTRUCTIONS>>>")
    elif show_instructions == "end":
        looping = False
    else:
        print("<<<ERROR>>>")
