def largest(min_factor, max_factor):
    x = [i for i in range(min_factor,max_factor+1)]
    # print(x)
    products = []
    palindromes = []
    num_str = []
    factors = []
    answer = []

    for j in x:
        for k in x:
            products.append(j*k)
        
    s = list(dict.fromkeys(products))
  
    for number in s:
        num_str.append(str(number))
   
    if len(num_str) == 1:
        return ( answer)
    else:
        for digits in num_str:

            # print(digits)
            if digits[::-1] == digits:
                palindromes.append(digits)
        # print(palindromes)
        largest_palindrome = int(palindromes[-1])
        # print(largest_palindrome)
        for m in range(1, largest_palindrome+1):
            if int(largest_palindrome) % m == 0:
                factors.append(m)
        # print(factors)
    
        for n in range(int((len(factors)/2+1))):
            answer.append([factors[n], factors[-(1+n)]])
            # print([factors[n], factors[-(1+n)]])
            print(largest_palindrome, answer)
            return (largest_palindrome, answer)


def smallest(min_factor, max_factor):
    x = [i for i in range(min_factor,max_factor+1)]
    products = []
    palindromes = []
    num_str = []
    factors = []

    for j in x:
        for k in x:
            products.append(j*k)
        
    s = list(dict.fromkeys(products))
  
    for number in s:
        num_str.append(str(number))
   
    for digits in num_str:
        print(digits)
        if digits[::-1] == digits:
            palindromes.append(digits)
    # print(palindromes)
    smallest_palindrome = int(palindromes[0])
    print(smallest_palindrome)
    for m in range(min_factor, smallest_palindrome+1):
        if smallest_palindrome % m == 0 and m != smallest_palindrome:
            factors.append(m)
    print(factors)
    answer = []
    for n in range(int((len(factors)/2+1))):
        answer.append([factors[n], factors[-(1+n)]])
        print([factors[n], factors[-(1+n)]])
        print(smallest_palindrome, answer)

        return (smallest_palindrome, answer)
#     x = [i for i in range(1,max_factor+1)]
#     products = []
#     palindromes = []
#     num_str = []

#     for j in x:
#         for k in x:
#             products.append(j*k)
        
#     s = list(dict.fromkeys(products))
  
#     for number in s:
#         num_str.append(str(number))
   
#     for digits in num_str:
#         # print(digits)
#         if digits[::-1] == digits:
#             palindromes.append(digits)
#     print(palindromes)
#     smallest_palindrome = palindromes[0]
#     print(smallest_palindrome)
#     for m in range(1, int(smallest_palindrome)+1):
#         if int(smallest_palindrome) % m == 0:
#             print(m)
            

largest(15,20)
smallest(1001,1001)