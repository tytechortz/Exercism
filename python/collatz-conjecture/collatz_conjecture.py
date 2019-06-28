def steps(number):
    step = 0
    if number < 1:
        raise ValueError("number must be 1 or greater")
    else:
        while number != 1:
            if number % 2 == 0:
                number = number / 2
                step += 1
            else:
                number = number * 3 + 1
                step += 1
    return step
