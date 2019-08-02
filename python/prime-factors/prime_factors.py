def factors(value):
    p_factors = []
    i = 2
    x = value

    while value % i != 1:
        if x % i == 0:
            p_factors.append(i)
            x = x / i
        else:
            i += 1
    print(p_factors)



factors(2)