def add(a,b):
    print('Addition',a+b)
    return a+b

def sub(a,b):
    print('Subtraction',a-b)
sub(3,5) #parameter passing



def mul(a,b):
    print('Multiplication',a*b)
mul(add(3,5),5)