def is_armstrong_number(number):
    digits = [int(x) for x in str(number)]
    digit_count = len(digits)
    # if sum([(y**digit_count) for y in digits]) == number:
    #     return True
    # else:
    #     return False
    return sum([(y**digit_count) for y in digits]) == number
