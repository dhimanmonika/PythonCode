"""A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages."""

from collections import Counter

#initialization using string
cnt1 =Counter("aabccdddde")
print("cnt1",cnt1)

#initialization using dict
cnt2=Counter({'a':1,'e':6})
print("cnt2",cnt2)

#initialization using arguments
cnt3=Counter(c=4,g=6)
print("cnt3",cnt3)

#accessing counter
#access using key
print("c occurs ",cnt1['c'] , "times in cnt1")

#access using elements()
print(list(cnt1.elements()))

#to find top three frequently occuring elements use most_common()
print(" three most common elements in cnt1")
print(cnt1.most_common(3))

#update operations on counter
#sum of all counts in cnt1
print(sum(cnt1.values()))

#reset counter
cnt1.clear()
cnt1 =Counter("aabccdddde") # reassigning

#arithmetic
print("addition of cnt1 and cnt2",cnt1+cnt2)

print("subtraction of cnt1 and cnt2",cnt1-cnt2)

print("intersection of cnt1 and cnt2",cnt1&cnt2)

print("union of cnt1 and cnt2",cnt1|cnt2)





