"""Fibonacci"""

def Fibonacci(number):
    a,b=0,1
    if number == 1:
        l=[a]
    elif number ==2:
        l=[a,b]
    else:
        l=[a,b]
        for i in range(number-2):
            c=a+b
            l.append(c)
            a=b
            b=c
    return l

if __name__=='__main__':
    number=int(input("Enter the number of elements for fibonacci"))
    myres=Fibonacci(number)
    print(myres)

