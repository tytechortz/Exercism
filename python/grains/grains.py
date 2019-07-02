def square(number):
    if number < 1 or number > 64:
        raise ValueError("number must be between 1 and 64")
    else:
        return int(2**number/2)

def total(number):
    if number < 1 or number > 64:
        raise ValueError("number must be between 1 and 64")
    else:
        return 2**number - 1
   


