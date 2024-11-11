from land import Square, Rectangular
from engineer import Engineer

def main():
    engineer = Engineer('Jaozao')
    square = Square(5)
    rectangular = Rectangular(4, 6)

    print(engineer.measureArea(square))
    print(engineer.measurePerimeter(square))
    print()
    print(engineer.measureArea(rectangular))
    print(engineer.measurePerimeter(rectangular))

if __name__ == '__main__':
    main()