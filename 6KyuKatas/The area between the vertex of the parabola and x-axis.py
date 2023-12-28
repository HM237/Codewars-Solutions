import math
def area(a, b, c):
    discriminant = (b**2)-(4*a*c)
    if discriminant < 0 or discriminant == 0: return 0
    else:
        root1 = ((-b) + math.sqrt(discriminant)) / (2*a)
        root2 = ((-b) - math.sqrt(discriminant)) / (2*a)
        a = a / 3
        b = b / 2
        x1 = (a * (root1**3)) + (b * (root1**2)) + (c * root1)
        x2 = (a * (root2**3)) + (b * (root2**2)) + (c * root2)
        area = abs(x2-x1)
        return area
