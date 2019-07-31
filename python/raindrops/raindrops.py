def convert(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    print(factors)



convert(15)