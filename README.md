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

(**) Create a class called Password with the following conditions:
It has the length and password attributes. By default, the length will be 8. The constructors will be as follows: A default constructor. A constructor with the length that we send as parameter. Generate a random password with that length. The methods you implement will be: isStrong (): return a boolean if it is strong or not, to be strong you must have more than 2 uppercase, more than 1 lower case and more than 5 numbers. GeneratePassword (): Generates the password of the object with the defined length. Get method for password and length. Set method for length. 
Now let’s create an executable class:
Create an array of Passwords with the size that you indicate by keyboard. Create a loop that creates an object for each position in the array. It also indicates by keyboard the length of the Passwords (before loop). Create another array of booleans where we store if the password of the password array is strong or not (use the previous loop). 
At the end, we show the password and whether or not it is strong (use the previous loop). Use this simple format: password1 boolean_value1
password2 boolean_value2. ---> [passwordClass.py](passwordClass.py)

(**) Develop a program to generate invoices to customers and purchase orders from suppliers.
The system displays a menu asking if you want to make an invoice or purchase order
In case of an invoice, it asks for the client’s data  and in case of being PO enter the supplier’s data.
Then the program asks to enter up to 10 items (may be less) with description and its value

At the end it calculates the net, GST, PST and finally shows on screen all the data of the invoice (or PO). One thing per line:
Invoice Number (PO)
Customer number (Supplier)
Customer name (Supplier)
Items with the value of each
Net
GST
PST
Total  
---> [invoiceAndPurchaseOrders.py](invoiceAndPurchaseOrders.py)
