class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def update_book_title(self,new_title):
        self.titse = new_title
    
    def update_author(self,new_author):
        self.author = new_author

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    