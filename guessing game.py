import random
x = random.randint(1, 10)
y = int(input("Guess what number I'm thinking of (1-10):\n"))
while x != y:
    if x < y:
        print("Too high, guess again!")
    if x > y:
        print("Too low, guess again!")
    y = int(input("Guess what number I'm thinking of (1-10):\n"))
print("You won! You're lucky - you won't win next time.")
