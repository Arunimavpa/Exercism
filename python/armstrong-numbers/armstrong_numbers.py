def is_armstrong_number(number):
    number_str = str(number)
    length=len(number_str)
    total=0
    for x in number_str:
        total += int(x)**length
    return total == number
    pass
