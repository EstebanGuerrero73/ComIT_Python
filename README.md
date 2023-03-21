# ComIT_Python
Practice problems with Python

(**) Create a class called Book that stores the information for each of the books in a library. 
The class should keep the title of the book, author, number of copies of the book and number of lend copies. The class will contain the following methods: Default constructor. Constructor with parameters. Setters / getters. Method Loan that increases the corresponding attribute each time a loan is made from the book. No books may be borrowed if no copies are available to lend. Returns true if the operation was successful and false otherwise. Returns method that decrements the corresponding attribute when a book is returned. No books can be returned that have not been lend. Returns true if the operation was successful and false otherwise. ToString method to display data from books. This method is inherited from Object and we must modify it (override) to adapt it to the Book class. Write a program to test the operation of the Book class. ---> [book_class.py](book_class.py)

(**) Implement the class Position that represents a coordinate (x, y). Each position is defined by two integer values ​​x and y. Available           operations are:
· Default constructor, corresponds to the position (0,0). 
· Constructor with initial values ​​of X and Y 
· Methods for modifying and querying (set / get) the attributes of the class. 
· Methods for increasing and decreasing the values ​​of each of the position coordinates (incX, incY, decX, decY). 
· A method for setting coordinate values ​​(setXY). ---> [coord_xy_class.py](coord_xy_class.py)
