def largest(min_factor, max_factor):
    x = [i for i in range(1,max_factor+1)]
    products = []
    palindromes = []
    num_str = []

    for j in x:
        for k in x:
            products.append(j*k)
        
    s = list(dict.fromkeys(products))
  
    for number in s:
        num_str.append(str(number))
   
    for digits in num_str:
        # print(digits)
        if digits[::-1] == digits:
            palindromes.append(digits)
    print(palindromes)
    largest_palindrome = palindromes[-1]
    print(largest_palindrome)
    for m in range(1, int(largest_palindrome)+1):
        if int(largest_palindrome) % m == 0:
            print(m)


# def smallest(min_factor, max_factor):
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
            

largest(1,9)
# smallest(1,9)