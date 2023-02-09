filename = "mytextfile.txt"
with open(filename, "r") as file:
    print(file.read())

mylist = ["a", "b", "c"]

for item in mylist:
    with open("mytextfile.txt", "a") as file:
        file.write(item)  # each item in the list
        file.write("\n")  # write a new line

with open("mytextfile.txt", "r") as file:
    print(file.read())
