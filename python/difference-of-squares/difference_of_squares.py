def square_of_sum(number):
    return int((number*(number+1)/2)**2)

def sum_of_squares(number):
    return int(round((number**3/3) + (number**2/2) + (number/6)))

def difference_of_squares(number):
    return int(round(square_of_sum(number) - sum_of_squares(number)))

