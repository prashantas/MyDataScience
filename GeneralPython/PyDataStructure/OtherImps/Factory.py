#### https://en.proft.me/2016/09/20/factory-design-pattern-java-and-python/
from abc import ABCMeta, abstractmethod

#######################FACTORY DESIGN PATTERN #################################
#Create base class.
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

#Create concrete classes implementing the same base class.
class Rectangle(Shape):
    def draw(self):
         print("Inside Rectangle::draw() method.")

class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")

class Circle(Shape):
    def draw(self):
        print("Inside Circle::draw() method.")        

##Create a Factory to generate object of concrete class based on given information.
class ShapeFactory(object):
    @staticmethod
    def get_shape(shape_type):
        if shape_type == 'CIRCLE':
            return Circle()
        elif shape_type == 'RECTANGLE':
            return Rectangle()
        elif shape_type == 'SQUARE':
            return Square()
        return None


##Use the Factory to get object of concrete class by passing an information such as type.
if __name__ == '__main__':        
    rectangle = ShapeFactory.get_shape('RECTANGLE')
    rectangle.draw()

    circle = ShapeFactory.get_shape('CIRCLE')
    circle.draw()

    square = ShapeFactory.get_shape('SQUARE')
    square.draw()
