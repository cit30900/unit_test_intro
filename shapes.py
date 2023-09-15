class Shape():

    def __init__(self, side1: float, side2: float):
        """ABSTRACT class - should never be instantiated"""
        self.side1 = side1
        self.side2 = side2
    
    @property # LOOKS like a method but is called like an attribute
    def area(self) -> float:
        pass

    @property
    def perimeter(self) -> float:
        pass

class Rectangle(Shape):

    def __init__(self, side1: float, side2: float):
        """Instantiate a new object of class Rectangle."""
        super().__init__(side1, side2)

    @property
    def area(self) -> float:
        """Calculates the area of a rectangle with the formula side1*side2"""
        return self.side1 * self.side2

    @property
    def perimeter(self) -> float:
        """Calculates the perimeter of a rectangle with the formula side1*2 + side2*2"""
        return self.side1 * 2 + self.side2 * 2
    
    @property
    def is_square(self) -> bool:
        """Returns T/F if rectangle is square"""
        if self.side1 == self.side2:
            return True
        else:
            return False


class Triangle(Shape):

    def __init__(self, side1: float, side2: float, side3: float, height: float):
        """Instantiate a new object of class Triangle."""
        self.side3 = side3
        self.height = height
        super().__init__(side1, side2)

    @property
    def area(self) -> float:
        """Calculates the area of a triangle with the formula (side3*height)/2"""
        return (self.side3 * self.height) / 2
    
    @property
    def perimeter(self) -> float:
        """Calculates the perimeter of a triangle with the formula side1+side2+side3"""
        return self.side1 + self.side2 + self.side3
    
    @property
    def is_valid(self) -> bool:
        """Returns T/F if triangle is valid"""
        if self.side1 + self.side2 >= self.side3 and self.side1 + self.side3 >= self.side2 and self.side2 + self.side3 >=self.side1:
            return True
        else:
            return False