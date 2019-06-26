def square_of_sum(number):
    print((number*(number+1)/2)**2)
    return int((number*(number+1)/2)**2)

def sum_of_squares(number):
    print((number**3/3) + (number**2/2) + (number/6))
    return int(round((number**3/3) + (number**2/2) + (number/6)))


def difference_of_squares(number):
    print(square_of_sum(number) - sum_of_squares(number))
    return int(round(square_of_sum(number) - sum_of_squares(number)))

difference_of_squares(1)