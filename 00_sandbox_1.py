import random

for i in range(0, 20):
    number = random.randint(0, 4)
    print(number, end='\n')

greeting = "hello world"
sides = "*" * 3

greeting = f"{sides}  {greeting}  {sides}"

top_bottom = "*" * len(greeting)

print(top_bottom)
print(greeting)
print(top_bottom)
