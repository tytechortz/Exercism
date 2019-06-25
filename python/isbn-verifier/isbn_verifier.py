def is_valid(isbn):
    isbn = list(isbn)
    
    if len(isbn) == 0:
        return False
    isbn[:] = [x for x in isbn if x != '-']
 
    if isbn[-1] == 'X':
        isbn[-1] = '10'
    
    isbn = [x for x in isbn if x.isdigit()]

    isbn = [int(i) for i in isbn]
    
    if len(isbn) == 10:
        if (isbn[0] * 10 + isbn[1] * 9 + isbn[2] * 8 + isbn[3] * 7 + isbn[4] * 6 + isbn[5] * 5 + isbn[6] * 4 + isbn[7] * 3 + isbn[8] * 2 + isbn[9] * 1) % 11 == 0:
            return True
        else:
            return False
    else:
        return False

