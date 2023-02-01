title = ' '
books = []
while title.lower() != 'q':
  title = input("what is the title of the book? (or q to quit): ")
  if title != 'q':
    books.qppend(title.title())
    print(f"'{title.capitalize()}' is {len(title)} characters in length.")
    print("The list is: ")
    print(books)
    print(50 * '=')
    print("The books you checked were")
    for idx, book in enumerate(books):
      print(f"{idx+1}: {book}")
      print(50 * '=')
