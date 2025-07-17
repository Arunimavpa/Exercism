def is_valid(isbn):
    total=0
    isbn=isbn.replace('-','')
    if len(isbn)!=10:
        return False
    if isbn[9] not in '1234567890X' :
        return False
    if not isbn[:9].isdigit() :
        return False
    total=0
    for i in range(9):
        total += (i+1) * int(isbn[i])
    if isbn[9]=='X':
        total +=10 * 10
    else:
        total +=10 * int(isbn[9])     
    return total % 11==0


    
