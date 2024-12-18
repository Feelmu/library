from Book import Book

class Member:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed:
            print(f"{book} is already borrowed")
        else:
            book.is_borrowed = True
            self.borrowed_books.append(book)

    def update_member_name(self,new_name):
        self.name = new_name
    
    def update_member_id(self,new_id):
        self.id = new_id

    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
        else:
            print(f"you did not borrow {book}")

    def __str__(self):
        borrowed_books = ', '.join([book.title for book in self.borrowed_books]) or "No books"
        return f"Member(name: {self.name}, ID: {self.id}, borrowed books: {borrowed_books})"
    
        