class Library:
    def __init__(self, booklist, libraryName):
        self.book = booklist
        self.name = libraryName
        self.lendDict = {}

    def displayBooks(self):
        print(f"\nWe have the following books in {self.name}:")
        for book in self.book:
            print(" -", book)

    def lendBook(self, user, book):
        if book not in self.book:
            print(f"❌ Sorry, '{book}' is not available in the library.")
        elif book not in self.lendDict:
            self.lendDict[book] = user
            print(f"✅ Lender-Book database has been updated. '{book}' is now issued to {user}.")
        else:
            print(f"⚠️ Sorry, '{book}' is already being used by {self.lendDict[book]}.")

    def addBook(self, book):
        self.book.append(book)
        print(f"✅ Book '{book}' has been added to the library.")

    def returnBook(self, book):
        if book in self.lendDict:
            self.lendDict.pop(book)
            print(f"✅ '{book}' has been returned.")
        else:
            print(f"⚠️ '{book}' was not issued.")

if __name__ == '__main__':
    centralLibrary = Library(['Python', 'C++', 'Java', 'Django'], "Central Library")

    while True:
        print(f"\nWelcome to the {centralLibrary.name}. Enter your choice:")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        print("5. Exit")

        choice = input(">>> ")

        if choice == "1":
            centralLibrary.displayBooks()
        elif choice == "2":
            user = input("Enter your name: ").capitalize()
            book = input("Enter the name of the book you want to lend: ").capitalize()
            centralLibrary.lendBook(user, book)
        elif choice == "3":
            book = input("Enter the name of the book you want to add: ").capitalize()
            centralLibrary.addBook(book)
        elif choice == "4":
            book = input("Enter the name of the book you want to return: ").capitalize()
            centralLibrary.returnBook(book)
        elif choice == "5":
            print("👋 Thanks for using the Library Management System!")
            break
        else:
            print("❌ Invalid Choice. Please try again.")
