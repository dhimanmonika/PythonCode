def bubble_sort(L):
    n =len(L)
    for i in range(n):

        for j in range(0,n-i-1):
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]


L=[32,1,4,67,45,3]
bubble_sort(L)
print(L)