from interfaces import ShapesInterface

class Engineer:
    def __init__(self, name):
        self.name = name

    def measurePerimeter(self, land: ShapesInterface):
        return f'Foi medido por {self.name}, o perimetro da forma como: {land.getPerimeter()}'
    
    def measureArea(self, land: ShapesInterface):
        return f'Foi medido por {self.name}, o perimetro da forma como: {land.getArea()}'