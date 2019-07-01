import itertools

def largest(min_factor, max_factor):
    pass


def smallest(min_factor, max_factor):
    x = [i for i in range(1,max_factor+1)]
    # x.append(i) for i in range(min_factor,max_factor+1)
    print(x)
    products = []
    for j in x:
        for k in x:

            products.append(j*k)
    # products = list(itertools.permutations(x))
        
    print(products)
    s = list(dict.fromkeys(products))
    print(s)
    

largest(1,9)
smallest(1,9)