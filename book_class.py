""" Create a class called Book that stores the information for each of the books in a library. 
The class should keep the title of the book, author, number of copies of the book and number of lend copies. 
The class will contain the following methods: Default constructor. Constructor with parameters. Setters / getters. 
Method Loan that increases the corresponding attribute each time a loan is made from the book. 
No books may be borrowed if no copies are available to lend. 
Returns true if the operation was successful and false otherwise. 
Returns method that decrements the corresponding attribute when a book is returned. 
No books can be returned that have not been lend. Returns true if the operation was successful and false otherwise. 
ToString method to display data from books. This method is inherited from Object and we must modify it 
(override) to adapt it to the Book class. Write a program to test the operation of the Book class. """

class Book:

    def __init__(self, title, author, copies, lended):
        self.title = title
        self.author = author
        self.copies = copies
        self.lended = lended

    def get_book(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Number of available copies: {self.copies}")
        print(f"Number of copies lended: {self.lended}")

    def set_book(self, title, author, copies, lended):
        self.title = title
        self.author = author
        self.copies = copies
        self.lended = lended

    def loan(self):
        if self.copies == 0:
            success = "False"
        else:
            self.copies -= 1
            self.lended += 1
            success = "True"
        print(f"\nLending was successful: {success}\n")

    def returns(self):
        if self.lended == 0:
            success = "False"
        else:
            self.copies += 1
            self.lended -= 1
            success = "True"
        print(f"\nReturning was successful: {success}\n")

    def __str__(self):
        return '\n\nTitle: ' + self.title + '\nAuthor: ' + self.author + \
            '\nNumber of available copies: ' + str(self.copies) + \
            '\nNunber of lended copies: ' + str(self.lended)

# Testing the class Book

book1 = Book("Vampires", "John Doe", 10, 2)
print(book1)
#book1.get_book()
book1.loan()
print(book1)
book1.returns()
print(book1)




        


    