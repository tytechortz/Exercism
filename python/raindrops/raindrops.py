def convert(number):
    factors = []
    drops = []
    listOfFactors = [3,5,7]
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    # print(factors)
    check = any(item in factors for item in listOfFactors)

    if check is True:
        for j in factors:
            if j == 3:
                drops.append("Pling")
            elif j == 5:
                drops.append("Plang")
            elif j == 7:
                drops.append("Plong")
        
        seperator = ''
        print(seperator.join(drops))
        return seperator.join(drops)
    else:
        print(number)
        return str(number)


convert(52)