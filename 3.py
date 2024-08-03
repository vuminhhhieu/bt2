class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def cal_area(self):
        return self.side_length ** 2

    def __str__(self):
        return f"Square(side_length={self.side_length})"
class Cube(Square):
    def cal_area(self):
        return 6 * (self.side_length ** 2)

    def cal_volume(self):
        return self.side_length ** 3

    def __str__(self):
        return f"Cube(side_length={self.side_length})"
square = Square(side_length=4)
print(square)  
print("Area of Square:", square.cal_area())  

cube = Cube(side_length=3)
print(cube)  
print("Surface Area of Cube:", cube.cal_area()) 
print("Volume of Cube:", cube.cal_volume())