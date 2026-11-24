class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r1 = rectangle(10, 5)
r2 = rectangle(8, 6)

if r1.area() > r2.area():
    print("rectangle 1 has a larger area")
elif r1.area() < r2.area():
    print("rectangle 2 has a larger area")
else:
    print("both rectangles have the same area")