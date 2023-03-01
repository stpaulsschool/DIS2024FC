
strings = "HeLlO"
capital = []
for index, letter in enumerate(strings):
    if letter.isupper():
        capital.append(index)
    return capital
print(strings("HeLlO"))

