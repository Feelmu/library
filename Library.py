from Book import Book
from Member import Member

class Library:
    def __init__ (self):
        self.books = []
        self.members = []
    
    def number_of_members(self):
        return len(self.members)
    
    def number_of_books(self):
        return len(self.books)
    
    def add_books(self, book):
        self.books.append(book)
    
    def remove_books(self,book):
        self.books.remove(book)
    
    def register_members(self,member):
        self.members.append(member)
    
    def remove_members(self,member):
        self.members.remove(member)
    
    def display_books(self):
        if not self.books:
            print("There is no book in Library")
        else:
            print("Books in Library")
            for book in self.books:
                status = "Not Available" if book.is_borrowed else "Available"
                print(f"{book} - {status}")

    def display_members(self):
        if not self.members:
            print("There is no member")
        else:
            for member in self.members:
                borrowed_books = ', '.join([book.title for book in member.borrowed_books ])if member.borrowed_books else "No book borrowed"
                print(f"{member.name} (ID: {member.id} - borrowed books: {borrowed_books} )")
