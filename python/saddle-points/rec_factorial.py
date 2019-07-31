def factorial(n):
    if n > 1:
        print(n)
        return factorial(n-1) * n
    else:
        return 1

factorial(4)