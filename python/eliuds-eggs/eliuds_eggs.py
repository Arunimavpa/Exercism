def egg_count(display_value):
    count=0
    while display_value>0 :
        rem= display_value%2
        count += rem
        display_value=display_value//2
    return count