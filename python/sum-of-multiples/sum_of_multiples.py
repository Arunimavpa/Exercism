def sum_of_multiples(limit, multiples):
    multiple=set()
    for num in multiples:
        if num==0:
            continue
        for i in range(num,limit,num):
            multiple.add(i)
    return sum(multiple)