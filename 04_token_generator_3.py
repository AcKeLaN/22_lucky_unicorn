import random

# Main Routine
tokens = ["unicorn", "zebra", "horse", "donkey"]
balance = 100

# Testing loop to generate 20 tokens
for i in range(0, 20):
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
