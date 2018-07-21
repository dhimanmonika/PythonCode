import random


def gen_random():
    return random.randint(1,21)


if  __name__=="__main__":
    R=gen_random()
    N,count=0,0
    l=[]
    while (R!=N):
        print("Enter your guess !!")
        N=int(input())
        if N not in l:
            l.append(N)
            count=count+1
        if N==R:
            break
        else:
            print("not equal to random number")
    print("you tried {} times to get answer {}".format(count,N))
    