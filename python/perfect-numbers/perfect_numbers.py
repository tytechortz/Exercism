def classify(number):
    factors = []

    if number <= 0:
        raise ValueError("Must use positive integer")
    else:
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


