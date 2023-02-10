import random
num = 1
guess = 0
count = 0
print("Welcome to the random number guessing game")
while guess != num:
    num = random.randint(0, 100)
    guess = random.randint(0, 100)
    count = count + 1
    print(count)
print("Congratulations, you guessed right in", count, "tries")
