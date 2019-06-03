def is_valid(isbn):
    print(isbn[-1])
    if isbn[-1] == 'X':
        new_isbn = isbn.replace(isbn[-1], '10', 1)

    # isbn = (''.join(i for i in isbn if i.isdigit()))
    
    print(new_isbn)

is_valid('3-598-21508-X')