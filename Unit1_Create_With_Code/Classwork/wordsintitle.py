book_title = input("What is the title of your book? (type q to quit)")
while book_title != "q":

    print("The book name is: " + book_title)
    res = len(book_title.split())
    print("The number of words in this book title are : " + str(res))
    if res <= 5:
        print("Your book would sell well on amazon based off of sales statistics.")
    else:
        print("A shorter book title would be better for your book")
    book_title = input("What is the title of your book? (type q to quit)")
