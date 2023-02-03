title = ' '
books = []
mydict = {}
length = []
while title.lower() != 'q':
    title = input("what is the title of the book? (or q to quit): ")
if title != 'q':
    books.append(title.title())
    print(f"'{title.capitalize()}' is {len(title)} characters in length.")
    print("The list is: ")
    print(books)
    print(50 * '=')
    print('The books you checked were')
    for idx, book in enumerate(mydict.items()):
        print(f"{idx + 1}: '{books}', has {length} characters")
        print(50 * '=')
        print("thanks, see you next time")
else:
    print("bye")
