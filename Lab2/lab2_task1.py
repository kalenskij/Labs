class Rectangle:

    def __init__(self, length=1.0, width=1.0):
        self.length = length
        self.width = width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @length.setter
    def length(self, length):
        if not isinstance(length, float):
            raise TypeError("Not float")
        if not 0 < length <= 20:
            raise ValueError("Wrong value")
        self.__length = length

    @width.setter
    def width(self, width):
        if not isinstance(width, float):
            raise TypeError("Not float")
        if not 0 < width <= 20:
            raise ValueError("Wrong value")
        self.__width = width

    def calculate_area(self):
        return self.length*self.width

    def calculate_perimeter(self):
        return (self.length+self.width)*2


a = Rectangle(2.0, 5.0)
print(a.calculate_area())
print(a.calculate_perimeter())
