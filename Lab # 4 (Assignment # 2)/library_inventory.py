# a list of dictionaries as library
library = [
    {'title': 'Java Masterclass', 'author': 'Tim Bach.', 'quantity': 12},
    {'title': 'C++ Masterclass', 'author': 'John Doe', 'quantity': 9},
    {'title': 'How To Fail As A Successful Superstar', 'author': 'Tom Holland', 'quantity': 15},
]


# returns True if book was found, else returns False
def searchByBookName(bookName):
    for book in library:
        if book['title'] == bookName:
            print(f"Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}\n")
            return True
    print("Book Not Found!\n")
    return False


# returns True if book was found, else returns False
def searchByAuthorName(authorName):
    for book in library:
        if book['author'] == authorName:
            print(f"Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}\n")
            return True
    print("Book Not Found!\n")
    return False


def addQuantityByBookName(bookName, addedQuantity):
    if type(addedQuantity) is not int:
        addedQuantity = int(addedQuantity)
    for book in library:
        if book['title'] == bookName:
            book['quantity'] += addedQuantity
            print("Quantity Added Successfully!\n")
            return True
    print("Book Not Found!\n")
    return False


def removeQuantityByBookName(bookName, subtractedQuantity):
    if type(subtractedQuantity) is not int:
        subtractedQuantity = int(subtractedQuantity)
    for book in library:
        if book['title'] == bookName:
            book['quantity'] -= subtractedQuantity
            print("Quantity Subtracted Successfully!\n")
            return True
    print("Book Not Found!\n")
    return False


# main function
while True:
    value = int(input(
    """
    1. Search by Book Name
    2. Search by Author Name
    3. Update the Quantity of a Book
    4. Quit
    Select An Option (1-4): """
    ))
    
    # 1. search by book name
    if value == 1:
        bookName = input("Enter the title of the book to be searched: ")
        searchByBookName(bookName)
        continue
    # 2. search by author name
    elif value == 2:
        authorName = input("Enter the author of the book to be searched: ")
        searchByAuthorName(authorName)
        continue
    # 3. update the quantity of a book
    elif value == 3:
        selection = int(input(
    """
    1. Add to Existing Quantity
    2. Subtract from Existing Quantity
    Select An Option (1 or 2): """))
        bookName = input("Enter the title of the book: ")
        if selection == 1:
            addedQuantity = input("Enter the quantity to add to the existing quantity: ")
            addQuantityByBookName(bookName, addedQuantity)
        elif selection == 2:
            subtractedQuantity = input("Enter the quantity to subtract from the existing quantity: ")
            removeQuantityByBookName(bookName, subtractedQuantity)
        else:
            print("Invalid Input!\n")
        continue
    # 4. quit
    else:
        break

