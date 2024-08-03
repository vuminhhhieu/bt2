class MathList:
    def __init__(self, values):
        if not all(isinstance(x, (int, float)) for x in values):
            raise ValueError("All elements in the list must be numbers.")
        self.values = values

    def __str__(self):
        return str(self.values)

    def __add__(self, number):
        if not isinstance(number, (int, float)):
            raise ValueError("Operand must be a number.")
        return MathList([x + number for x in self.values])

    def __sub__(self, number):
        if not isinstance(number, (int, float)):
            raise ValueError("Operand must be a number.")
        return MathList([x - number for x in self.values])

math_list = MathList([1, 2, 3, 4, 5])
print(math_list)

math_list += 2
print(math_list)

 