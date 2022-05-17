import random

# Main Routine
STARTING_BALANCE = 100

balance = STARTING_BALANCE

# Testing loop to generate 20 tokens
for i in range(0, 100):
    chosen_num = random.randint(1, 100)

    # Adjust balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    else:
        chosen = "horse / zebra"
        balance -= 0.5

    # Output
    print(f"Token: {chosen} / Balance: ${balance}")

print(f"Starting Balance: ${STARTING_BALANCE:.2f}")
print(f"Final Balance: ${balance:.2f}")
