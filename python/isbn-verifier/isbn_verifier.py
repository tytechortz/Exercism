def is_valid(isbn):
    isbn = list(isbn)
    # print(isbn)
    if len(isbn) == 0:
        return False
    isbn[:] = [x for x in isbn if x != '-']
    # print(isbn)
    if isbn[-1] == 'X':
        isbn[-1] = '10'
    # print(isbn)
    # isbn = ''.join(map(str, isbn))
    # isbn = list(isbn)
    # print(isbn)
    isbn = [x for x in isbn if x.isdigit()]
    isbn = [int(i) for i in isbn]
    # print(isbn[0])
    # print(len(isbn))
    if len(isbn) == 10:
        if (isbn[0] * 10 + isbn[1] * 9 + isbn[2] * 8 + isbn[3] * 7 + isbn[4] * 6 + isbn[5] * 5 + isbn[6] * 4 + isbn[7] * 3 + isbn[8] * 2 + isbn[9] * 1) % 11 == 0:
            # print('good isbn')
            return True
        else:
            # print('invalid')
            return False
    else:
        # print('invalid')
        return False

# is_valid('3-598-P1581-X')