def is_triangle(sides):
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False
    
    if sides[0] + sides[1] < sides[2] or sides[1] + sides[2] < sides[0] or sides[2] + sides[0] < sides[1]:
        return False
    
    return True

def equilateral(sides):
    if not is_triangle(sides):
        return False
    
    if sides[0] + sides[1] == sides[2] * 2:
        return True
    
    return False


def isosceles(sides):
    if not is_triangle(sides):
        return False
    
    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return True
    
    return False


def scalene(sides):
    if not is_triangle(sides):
        return False
    
    if not (equilateral(sides) or isosceles(sides)):
        return True
    
    return False
