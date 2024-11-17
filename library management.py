class Library:
    def __init__(self,books):
        self.books=books
        print("Welcome to Library")
    def display_books(self):
        print("Books available:")
        for book in self.books:
            print(f"{book}")    
        print()
    def lend_book(self,book):
        if book in self.books:
            self.books.remove(book)
            print(f"you borrowed this'{book}, enjoy reading")
        else:
            print("sorry book not available")
    def return_book(self,book):
        self.books.append(book)   
        print(f"thank u for returning the book")
    def add_book(self,book):
        self.books.append(book)
        print(f"the book {book} is added")
    def __del__(self):
        print("thank u for visiting ")
library=Library(["Rich Dad Poor Dad","War and Peace","Harry Potter","Crime and Punishment"]) 
library.display_books()
library.lend_book("Harry Potter")
library.return_book("Harry Potter")
