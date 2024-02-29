import math

def square(side):
    area = side * side
    if not area.is_integer():
        area = math.ceil(area)
    return area


side = 5
square_area = square(side)


print("Площадь квадрата со стороной", side, ":", square_area)
