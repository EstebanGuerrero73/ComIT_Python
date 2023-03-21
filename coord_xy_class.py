"""   Implement the class Position that represents a coordinate (x, y).
  Each position is defined by two integer values ​​x and y. Available operations are:
· Default constructor, corresponds to the position (0,0). 
· Constructor with initial values ​​of X and Y 
· Methods for modifying and querying (set / get) the attributes of the class. 
· Methods for increasing and decreasing the values ​​of each of the position 
  coordinates (incX, incY, decX, decY). 
· A method for setting coordinate values ​​(setXY). """

class Position:
    def __init__(self, x_coord = 0, y_coord = 0):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def setXY(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def get(self):
        print(f"Coordinates = ({self.x_coord}, {self.y_coord})")

    def incX(self, x_inc):
        self.x_coord += x_inc

    def decX(self, x_dec):
        self.x_coord -= x_dec    

    def incY(self, y_inc):
        self.y_coord += y_inc

    def decY(self, y_dec):
        self.y_coord -= y_dec

# Testing the class Position

p1 = Position()
p2 = Position(5, 10)
p1.get()
p2.get()
p1.setXY(15, 30)
p2.incX(4)
p2.decY(2)   
p1.get()
p2.get()