class Book:
    def __init__(self, book_id, title, author, is_issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = is_issued

    def display_book(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"Book ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Status  : {status}")


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print("Book ID already exists")
        else:
            self.books[book_id] = Book(book_id, title, author)
            print("Book added successfully")
            save_books(self.books)

    def issue_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if not book.is_issued:
                book.is_issued = True
                print("Book issued successfully")
                save_books(self.books)
            else:
                print("Book already issued")
        else:
            print("Book not found")

    def return_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if book.is_issued:
                book.is_issued = False
                print("Book returned successfully")
                save_books(self.books)
            else:
                print("Book was not issued")
        else:
            print("Book not found")
    def search_book(self, book_id):
        if book_id in self.books:
            print("Book found:")
            self.books[book_id].display_book()
        else:
            print("Book not found")
    def delete_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            save_books(self.books)
            print("Book deleted successfully")
        else:
            print("Book not found")

    def display_books(self):
        if not self.books:
            print("No books available")
            return

        total = len(self.books)
        issued = sum(book.is_issued for book in self.books.values())

        print("\n========= LIBRARY BOOK LIST =========")
        for book in self.books.values():
            print("-----------------------------------")
            book.display_book()
        print("-----------------------------------")
        print(f"Total Books  : {total}")
        print(f"Issued Books : {issued}")
        print(f"Available    : {total - issued}")




def load_books():
    books = {}
    try:
        with open("library.txt", "r") as file:
            for line in file:
                book_id, title, author, is_issued = line.strip().split(",")
                books[int(book_id)] = Book(
                    int(book_id),
                    title,
                    author,
                    is_issued == "True"
                )
    except FileNotFoundError:
        pass
    return books


def save_books(books):
    with open("library.txt", "w") as file:
        for book in books.values():
            file.write(
                f"{book.book_id},{book.title},{book.author},{book.is_issued}\n"
            )



library = Library()
library.books = load_books()

while True:
    print("""
1. Add book
2. Issue book
3. Return book
4. Display books
5. Search book
6. Delete book
7. Exit
""")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Enter book ID: "))
        title = input("Enter title: ")
        author = input("Enter author: ")
        library.add_book(book_id, title, author)

    elif choice == 2:
        book_id = int(input("Enter book ID to issue: "))
        library.issue_book(book_id)

    elif choice == 3:
        book_id = int(input("Enter book ID to return: "))
        library.return_book(book_id)

    elif choice == 4:
        library.display_books()
    elif choice == 5:
        book_id = int(input("Enter book ID to search: "))
        library.search_book(book_id)

    elif choice == 6:
        book_id = int(input("Enter book ID to delete: "))
        library.delete_book(book_id)

    elif choice == 7:
        print("Data saved. Exiting...")
        save_books(library.books)
        break

    else:

        print("Invalid choice")
