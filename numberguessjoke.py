import random
num = random.randint(0, 100)
count = 0
print("Welcome to the random number guessing game. You have 6 tries to guess a number 0-100")
guess1 = int(input("what number is your guess?"))
if guess1 < num:
    print("wrong guess, try guessing higher")
else:
    print("not quite, try guessing lower.")
guess2 = int(input("what number is your guess?"))
if guess2 < num:
    print("wrong guess, try guessing higher")
else:
    print("not quite, try guessing lower.")
guess3 = int(input("what number is your guess?"))
if guess3 < num:
    print("wrong guess, try guessing higher")
else:
    print("not quite, try guessing lower.")
guess = int(input("what number is your guess?"))
if guess < num:
    print("wrong guess, try guessing higher")
else:
    print("not quite, try guessing lower.")
guess = int(input("what number is your guess?"))
if guess < num:
    print("wrong guess, try guessing higher")
else:
    print("not quite, try guessing lower.")
guess = int(input("what number is your guess?"))
if guess < num:
    print("wrong guess, try guessing higher")
else:
    print("not quite, try guessing lower.")





