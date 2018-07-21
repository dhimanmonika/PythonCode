
def insertion_sort(L):
    for i in range(1,len(L)):
        key=L[i]
        j=i-1
        while j>=0 and L[j]>key:
            L[j+1]=L[j]
            j=j-1
        L[j+1]=key

if __name__=="__main__":
    L=[2,34,13,23,4,7,10]
    insertion_sort(L)
    print(L)