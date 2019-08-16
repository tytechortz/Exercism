def convert(number):
    listOfFactors = [3,5,7]
    drops = []

    for i in listOfFactors:
        if number % i == 0:
            if i == 3:
                drops.append("Pling")
            elif i == 5:
                drops.append("Plang")
            elif i == 7:
                drops.append("Plong")
        
    if len(drops) == 0:
        return number
    else:
        separator = ''
        return separator.join(drops)

