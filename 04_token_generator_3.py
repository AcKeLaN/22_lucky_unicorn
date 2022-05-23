import random


# Functions
def token_generator():

    starting_balance = 100
    balance = starting_balance

    # Testing loop to generate 20 tokens
    for i in range(0, 10):
        chosen_num = random.randint(1, 100)

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
        print(f"Token: {chosen} / Balance: ${balance}")

    print(f"Starting Balance: ${starting_balance:.2f}")
    print(f"Final Balance: ${balance:.2f}")


# Main Routine
