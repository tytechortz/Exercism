def largest(min_factor, max_factor):
    pass


def smallest(min_factor, max_factor):
    x = [i for i in range(1,max_factor+1)]
    # print(x)
    products = []
    palindromes = []
    num_str = []
    for j in x:
        for k in x:
            products.append(j*k)
        
    # print(products)
    s = list(dict.fromkeys(products))
    print(s)
    for number in s:
        num_str.append(str(number))
    print(num_str)

    print(num_str[-1])
    print(num_str[-1][::-1])
    
    for digits in num_str:
        # print(digits)
        if digits[::-1] == digits:
            palindromes.append(digits)
    print(palindromes)


largest(1,9)
smallest(1,9)