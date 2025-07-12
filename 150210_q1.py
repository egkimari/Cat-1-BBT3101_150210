class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"You borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"You returned '{book.title}'")
        else:
            print(f"You did not borrow '{book.title}'")

    def list_borrowed_books(self):
        if not self.borrowed_books:
            print("You haven't borrowed any books.")
        else:
            print("Your borrowed books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")


if __name__ == "__main__":
    books = [
        Book("1984", "George Orwell"),
        Book("Python Basics", "Guido van Rossum"),
        Book("Clean Code", "Robert C. Martin")
    ]

    name = input("Enter your name: ")
    member_id = input("Enter your member ID: ")
    member = LibraryMember(name, member_id)

    while True:
        print("\nMenu:")
        print("1. View available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. View borrowed books")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            for i, book in enumerate(books):
                status = "Available" if not book.is_borrowed else "Borrowed"
                print(f"{i + 1}. {book.title} by {book.author} [{status}]")
        elif choice == "2":
            print("\nBooks you can borrow:")
            for i, book in enumerate(books):
                if not book.is_borrowed:
                    print(f"{i + 1}. {book.title}")
            try:
                num = int(input("Enter book number to borrow: ")) - 1
                member.borrow_book(books[num])
            except:
                print("Invalid selection.")
        elif choice == "3":
            if not member.borrowed_books:
                print("You haven't borrowed any books.")
                continue
            for i, book in enumerate(member.borrowed_books):
                print(f"{i + 1}. {book.title}")
            try:
                num = int(input("Enter book number to return: ")) - 1
                member.return_book(member.borrowed_books[num])
            except:
                print("Invalid selection.")
        elif choice == "4":
            member.list_borrowed_books()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
