from interfaces import ShapesInterface

class Rectangular(ShapesInterface):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def getPerimeter(self):
        return (self.__width * 2) + (self.__height * 2)
    
    def getArea(self):
        return self.__width * self.__height