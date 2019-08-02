def factors(value):
    i = 2
    p_factors = []

    if value <= 3 and value > 1:
        return [value]
    else:
        while value > 1:
            if value % i == 0:
                p_factors.append(i)
                value = value / i
            else:
                i += 1
    
    return p_factors

print(factors(1))