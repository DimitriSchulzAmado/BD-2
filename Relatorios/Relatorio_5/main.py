from src.database import Database
from src.bookModel import BookModel

db = Database(database="relatorio_5", collection="books")
book_model = bookModel(database=db)

while True:
    # Displaying menu options
    print("\n--- MENU ---")
    print("1. Create a book")
    print("2. Search a book by ID")
    print("3. Update a book")
    print("4. Remove a book")
    print("0. LogOut")

    # Prompting user choice
    choice = input("Choose an option: ")

    # Performing the operation corresponding to the user's choice
    if choice == "1":
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        year = int(input("Enter the year of the book: "))
        price = float(input("Enter the price of the book: "))
        book_model.create_livro(title, author, year, price)
    elif choice == "2":
        id_book = input("Write the book ID: ")
        book_model.read_livro_by_id(id_book)
    elif choice == "3":
        id_book = input("Enter the ID of the book you want to update: ")
        title = input("Enter the new book title: ")
        author = input("Enter the new author of the book: ")
        year = int(input("Enter the new year of the book: "))
        price = float(input("Enter the new book price: "))
        book_model.update_livro(id_book, title, author, year, price)
    elif choice == "4":
        id_book = input("Enter the ID of the book you want to delete:")
        book_model.delete_livro(id_book)
    elif choice == "0":
        print("Leaving the program...")
        break
    else:
        print("Invalid option. Please choose a valid option.")
            