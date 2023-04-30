with open("books_and_chapters.txt") as books:
    largest_book = ""
    largest_book_chapters = 0

    for line in books:
        book = line.split(":")
        # Scripture: Old Testament, Book: Genesis, Chapters: 50
        # print(f"Scripture: {book[0]}, Book: {book[2].strip()}, Chapters: {book[1]}")

        if (int(book[1]) > int(largest_book_chapters)):
            largest_book_chapters = book[1]
            largest_book = book[0].strip()
    print(f"The largest book is {largest_book} with {largest_book_chapters} chapters")