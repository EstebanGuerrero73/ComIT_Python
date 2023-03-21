'''Create a class called Password with the following conditions:
It has the length and password attributes. By default, the length will be 8. The constructors will be as follows:
A default constructor. A constructor with the length that we send as parameter. Generate a random password with that 
length. The methods you implement will be: isStrong (): return a boolean if it is strong or not, to be strong you 
must have more than 2 uppercase, more than 1 lower case and more than 5 numbers. 
GeneratePassword (): Generates the password of the object with the defined length. Get method for password and length. 
Set method for length. 
Now let’s create an executable class:
Create an array of Passwords with the size that you indicate by keyboard. Create a loop that creates an object 
for each position in the array. It also indicates by keyboard the length of the Passwords (before loop). 
Create another array of booleans where we store if the password of the password array is strong or not 
(use the previous loop). 
At the end, we show the password and whether or not it is strong (use the previous loop). Use this simple format: 
password1 boolean_value1
password2 boolean_value2'''



class Password:
    def __init__(self, length = 8, password = "00000000"):
        self.length = length
        self.password = password

    def GeneratePassword(self):
        '''Create a random character including:
        1. Numbers from 0 - 9
        2. Letters from a - z
        3. Letters from A - Z'''
        import random
        # Creating a list with all the possible characters
        char_list = []
        password_list = []
        password_string = ""
        # Adding lowercase letters
        for i in range(97,123):
            char_list.append(chr(i))
        # Adding uppercase letters
        for i in range(65,91):
            char_list.append(chr(i))
        # Adding numbers
        for i in range(48,58):
            char_list.append(chr(i))
        # Creating the password using random indexes
        for i in range(self.length):
            random_index = random.randint(0, 61)
            password_list.append(char_list[random_index])
        for i in password_list:
            password_string += i
        self.password = password_string

    def get(self):
        print(f"\nLength: {self.length}\tPassword: {self.password}\tStrong password: {self.isStrong()}\n")

    def setLength(self, length):
        self.length = length

    def isStrong(self):
        lowerCase = 0
        upperCase = 0
        numbers = 0
        # Check for lowercase letters
        for i in self.password:
            if (ord(i) > 97) and (ord(i) < 122): 
                lowerCase += 1

        # Check for uppercase letters
        for i in self.password:
            if (ord(i) > 65) and (ord(i) < 90):
                upperCase += 1

        # Check for numbers
        for i in self.password:
            if (ord(i) > 48) and (ord(i) < 57):
                numbers += 1

        if (upperCase > 2) and (lowerCase > 1) and (numbers > 5):
            return True
        else:
            return False



# Code to test Password class

print("\n\n\n   * * *   TEST OF PASSWORD CLASS   * * *   ")
numberOfPasswords = int(input("\nPlease enter the number of passwords: "))
print("\n")
passwordsList = []
for i in range(numberOfPasswords):
    passwordLength = int(input(f"\nPlease enter the lenght of password {i+1}: "))
    passwordsList.append(Password(passwordLength))

print("\n\n\n   * * *   TABLE OF PASSWORDS   * * *   ")

for i in range(numberOfPasswords):
    passwordsList[i].GeneratePassword()
    passwordsList[i].get()
print("   * * * * * * * * * * * * * * * * * * *   ")
input("\nPlease press Enter to exit ...")

    