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

def rec(n):

    if n<=0:
        print("wrong input")
    if n==1:
        return 0
    if n ==2:
        return 1
    else:
        return rec(n-1)+rec(n-2)



if __name__=='__main__':
    number=int(input("Enter the number of elements for fibonacci"))
    myres=Fibonacci(number)
    print(myres)
    for i in range(1,number+1):
        print(rec(i), end=" ")

