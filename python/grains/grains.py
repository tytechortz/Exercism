def square(number):
    if number < 1 or number > 64:
        raise ValueError("number mjust be between 1 and 64")
    else:
        print(int(2**number/2))
        return int(2**number/2)


def total(number):
    if number < 1 or number > 64:
        raise ValueError("number mjust be between 1 and 64")

    else:
    # for x in range(1,number+1):
        fun = 2**number - 1
        
    print(fun)
    return(fun)


square(4)
total(20)