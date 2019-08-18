def convert(number):
    
    factors = {3:"Pling",5:"Plang",7:"Plong"}
    drops = []

    for i in factors:
        if number % i == 0:
            drops.append(factors.get(i))
   
    if not drops:
        return str(number)
    else:
        separator = ''
        return separator.join(drops)

