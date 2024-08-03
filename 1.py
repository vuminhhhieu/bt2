class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return f"Rectangle object with heigh = {self.height} and width = {self.width}"

rect = Rectangle(height=2, width=1)
print(rect)  