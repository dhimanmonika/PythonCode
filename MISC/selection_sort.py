def selection_sort(L):
    for i in range(len(L)):
        min_idx=i
        for j in range(i+1,len(L)):
            if L[min_idx]>L[j]:
                min_idx=j
        L[i],L[min_idx]=L[min_idx],L[i]
    print(L)

selection_sort([8,6,5,3,2])





