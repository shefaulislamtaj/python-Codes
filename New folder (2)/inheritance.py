class Shape: 
    def __init__(self, diml, diml2): 
        self.diml = diml
        self.diml2 = diml2 
        
    def area(self):
        print("I am the area method of the Shape class.")  
        
        
class Triangle(Shape):  
    def area(self):
        
        area = 0.5 * self.diml * self.diml2
        print(f"Area of the triangle: {area}")


t = Triangle(10, 20)
t.area()  