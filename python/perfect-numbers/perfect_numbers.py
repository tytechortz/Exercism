def classify(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    
    sum_of_factors = sum(factors[:-1])
    if sum_of_factors == number:
        return 'perfect'
    elif sum_of_factors > number:
        return "abundant"
    else:
        return "deficient"


