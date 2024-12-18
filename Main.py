from Book import Book
from Member import Member
from Library import Library

def main():
    print("\n=========================================== Library App ===========================================\n")
    print("Student: Jeonghu Heo\n")
    book1 = Book("To Kill a Mochingbird", "Harper Lee")
    book2 = Book("1984", "George Orwell")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    member1 = Member("Avdyrahman Agajykov" , 123001)
    member2 = Member("Hassan Mroue", 123002)
    member3 = Member("Jeonghu Heo", 123003)
    
    chris_library = Library()
    chris_library.register_members(member1)
    chris_library.register_members(member2)
    chris_library.register_members(member3)

    chris_library.add_books(book1)
    chris_library.add_books(book2)
    chris_library.add_books(book3)

    

    print("\n=========================================== Status  ===========================================\n")

    print(f"Number of Active Members: {chris_library.number_of_members()}")
    print(f"Number of Active Books: {chris_library.number_of_books()}")

    print("\n=========================================== Display Books ===========================================\n")
    chris_library.display_books()
    print("\n=========================================== Display Members ===========================================\n")
    chris_library.display_members()

    #Tracking Operations:
    member1.borrow_book(book1)
    member2.borrow_book(book2)

    print("\n=========================================== Display after borrow===========================================\n")
    chris_library.display_members()

    chris_library.display_books()

    print("\n=========================================== Return Books ===========================================\n")
    member1.return_book(book1)
    chris_library.display_members()

    
    #Remove
    print("\n=========================================== Remove Member  ===========================================\n")
    chris_library.remove_members(member1)
    print(f"Removed Member: {member1}")

    chris_library.display_members()

    print("\n=========================================== Remove Books ===========================================\n")
    chris_library.remove_books(book1)
    chris_library.display_books()

    print("\n=========================================== Update Books ===========================================\n")
    book3.update_book_title("The Greatest Gatsby")
    book3.update_author("Chris")
    chris_library.display_books()

    print("\n=========================================== Update Members ===========================================\n")
    member3.update_member_name("Chris Heo")
    member3.update_member_id("123005")
    chris_library.display_members()

    print("\n=========================================== Library App ===========================================")


    
    

main()