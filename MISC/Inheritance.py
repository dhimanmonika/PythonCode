"""
"""

class Polygon:
    def __init__(self,nofSides):
        self.n=nofSides
        self.sides=[0 for i in range (self.n)]

    def SidesOfPolygon(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]

    def  DispSides(self):
        for i in range(self.n):
            print(" The side ", str(i+1)," of polygon is : ",self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        print("Polygon is Triangle ")
        Polygon.__init__(self,3)

    def FindArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print("The area of Triangle is : %0.2"%area)


t=Triangle
t.SidesOfPolygon()
t.DispSides()
t.FindArea()