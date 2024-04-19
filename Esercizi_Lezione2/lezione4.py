def substract (a:float, b:float):
    result= a - b
    return result

a= 3.5
b= 2
result= substract(3.5, 2)
print (result)





###

def check_value(n: int, check:int):
    if n > check:
        print (f' {n} è più grande di {check}')
    elif n > check:
        print (f' {n} è più piccolo di {check}')
    else:
        print (f' {n} è uguale a {check}')

check_value(10, 5)


###

def check_length (s: str):
    
    if len(s) > 10:
        print (f' {s} è più piccolo di 10 chars')
    elif len(s) < 10:
        print (f' {s} è più piccolo di 10 chars')
    else:
        print (f' {s} è uguale a 10 chars')

res=check_length("ciccio")
