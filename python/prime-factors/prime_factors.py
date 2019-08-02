def factors(value):
    factors = []
    divisors = []
    i = 2
    for x in range(i,value//2+1):
        if value % x == 0:
            factors.append(x)


    print(factors)
    # for x in range(i,int(value/2+1)):
    #     if value % x == 0:
    #         factors.append(x)
    #         if value/x % x == 0:
    #             factors .append(x)
    #     # else:
    #     #     i += 1
    # print(factors)
    

factors(60)