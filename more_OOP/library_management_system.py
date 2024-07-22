class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"

book1 = Book("Start with Why","simon sinek" )    
book2 = Book("The Alchemist","Paulo Coelho" )    
book3 = Book("Pride and Prejudice","Jane Austen" ) 

print(book1)
print(book2)
print(book3)
    

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        self.card_number = []
    def borrow_books(self, book):
        self.borrowed_books.append(book)
    
    def add_card_number(self, number):
        self.card_number.append(number)
    
    def __str__(self):
        return f"Member: {self.name} Borrowed books: {[str(book) for book in self.borrowed_books]} card_number:{[str(book) for book in self.card_number]}"
    
   
member1 = Member("Simon")
member2 = Member("Paulo")
member1.add_card_number(324)
member2.add_card_number(4554)
member1.borrow_books(book1)
member2.borrow_books(book2)
member2.borrow_books(book2)
print(member1)
print(member2)

class Library:
    library = "Default library"
    total_books = 0
    def __init__(self, name):
        self.name = name
        self.book_object = []
        self.members_object = []

    def add_book(self, book):
        self.book_object.append(book)
        Library.total_books += 1

    def add_member(self, mem):
        self.members_object.append(mem)
        