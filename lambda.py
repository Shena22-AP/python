#normal function:
def square (a):
    return a*a

#lambda function:
square = lambda a:a*a
rectangle = lambda a , b :a*b
triangle = lambda a , b : 0.5*a*b
print("square :", square (5))
print("rectangle :", rectangle (5,4))
print("triangle :", triangle (6,4)) 