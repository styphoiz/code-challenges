def maximum(num1,num2,num3):
    a = num1
    if(num2>a):
        a=num2
    if(num3>a):
        a=num3
    return a

def max_any(*args):
    a = 0
    for i in args:
        if(i>a):
            a = i
    return a 

#test
print(maximum(1,5,7))
print(maximum(5,7,1))
print(maximum(7,5,1))
print(max_any(7,5,1,33,54,42,99))
print(max_any(7,78,5,62,1))
print(max_any(65,12,7,5,1))

