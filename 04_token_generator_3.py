import random

# Main Routine
tokens = ["unicorn", "zebra", "zebra", "zebra",
          "horse", "horse", "horse",
          "donkey", "donkey", "donkey"]

STARTING_BALANCE = 100

balance = STARTING_BALANCE

# Testing loop to generate 20 tokens
for i in range(0, 500):
    chosen = random.choice(tokens)

    # Adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

    # Output
    print(f"Token: {chosen} / Balance: ${balance}")

print(f"Starting Balance: ${STARTING_BALANCE:.2f}")
print(f"Final Balance: ${balance:.2f}")
