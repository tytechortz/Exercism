import math

def score(x, y):
    points = 0
    if math.sqrt(x**2 + y**2) <= 1:
        points += 10
    elif math.sqrt(x**2 + y**2) > 1 and math.sqrt(x**2 + y**2) <= 5:
        points += 5
    elif math.sqrt(x**2 + y**2) > 5 and math.sqrt(x**2 + y**2) <= 10:
        points += 1
    return points


    
