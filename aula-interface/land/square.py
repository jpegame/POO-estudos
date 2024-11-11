from interfaces import ShapesInterface

class Square(ShapesInterface):
    def __init__(self, side):
        self.__side = side

    def getPerimeter(self):
        return self.__side * 4
    
    def getArea(self):
        return self.__side ** 2