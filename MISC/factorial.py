

def find_fact(n):
    if n ==1:
        return 1
    else:
        f=1
        for i in range(1,n+1):
            f=i*f
        return f


if __name__ =="__main__":
    T=int(input())
    for i in range(T):
        n=int(input())
        print("factorial of {} is {}".format(n,find_fact(n)))

