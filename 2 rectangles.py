
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()


# Getting dimensions of rectangle 1
l1 = float(input("Enter length of rectangle 1: "))
w1 = float(input("Enter width of rectangle 1: "))

# Getting dimensions of rectangle 2
l2 = float(input("Enter length of rectangle 2: "))
w2 = float(input("Enter width of rectangle 2: "))

# Creating objects
r1 = Rectangle(l1, w1)
r2 = Rectangle(l2, w2)

# Comparing areas
if r1 < r2:
    print("Rectangle 1 has smaller area")
elif r2 < r1:
    print("Rectangle 2 has smaller area")
else:
    print("Both rectangles have equal area")
