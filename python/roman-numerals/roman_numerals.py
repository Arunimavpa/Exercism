def roman(number):
    roman_no=[
            ("M",1000),
           ("CM",900),
           ("D",500),
           ("CD",400),
           ("C",100),
           ("XC",90),
           ("L",50),
           ("XL",40),
           ("X",10),
           ("IX",9),
           ("V",5),
           ("IV",4),
           ("I",1)
           ]
    result=""
    for symbol, value in roman_no:
        while number >=value:
            number-=value
            result+=symbol
    return result