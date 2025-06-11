def Triangle(a,b,c):
     return (a + b >= c) and (b + c >= a) and (a + c >= b)
def equilateral(sides):
    a,b,c=sides
    return a==b==c!=0 if Triangle(a,b,c) else False
      
def isosceles(sides):
    a,b,c=sides
    return a==b or b==c or c==a if Triangle(a,b,c) else False


def scalene(sides):
    a,b,c=sides
    return a!=b and b!=c and c!=a  if Triangle(a,b,c) else False
