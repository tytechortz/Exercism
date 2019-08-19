def classify(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors
    
def check(factors, number):
        sum_of_factors = sum(factors[:-1])
        if sum_of_factors == number:
            return 'perfect'
        elif sum_of_factors > number:
            return "abundant"
        else:
            return "deficient"
        # return sum_of_factors
            



# print(classify(6))
# print(check(classify(30), 30))