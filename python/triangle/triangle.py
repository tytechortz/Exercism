def equilateral(sides):
    sides.sort()
    print(sides)
    print(max(sides))
    if 0 not in sides and max(sides) <= sides[0] + sides[1]:
        print(len(set(sides)) <= 1)
        return len(set(sides)) <= 1 
    else:
        return False

def isosceles(sides):
    sides.sort()
    if 0 not in sides and max(sides) <= sides[0] + sides[1]:
        return len(set(sides)) <= 2
    else:
        return False

def scalene(sides):
    sides.sort()
    if 0 not in sides and max(sides) <= sides[0] + sides[1]:
        return len(set(sides)) == 3
    else:
        return False

# equilateral([0,0,0])