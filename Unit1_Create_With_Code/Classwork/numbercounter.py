import random
num = random.randint(0, 100)
guess = 101
count = 0
print("Welcome to the random number guessing game")
while guess != num:
    count = count + 1
    guess = int(input("what number is your guess?"))
    if guess < num:
        print("wrong guess, try guessing higher")
    else:
        print("not quite, try guessing lower.")
print("Congratulations, you guessed right in", count, "tries")


