# Statement Generator for titles
def statement_gen(statement, decoration):

    sides = decoration * 3

    statement = f"{sides}  {statement}  {sides}"

    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main Routine
statement_gen("Welcome to the Lucky Unicorn Game", "*")

