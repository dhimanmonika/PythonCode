l=[1,1,1,1,1,1,1]

m_no=max(l)
print(m_no)


#secondlargest
l1,l2=0,0
for i in l:
    if i>=l1:
        l2=l1
        l1=i

print("second largest number is {}".format(l2))
