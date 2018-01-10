"""
A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed).
However, the set itself is mutable. We can add or remove items from it.
"""
# set of integers
my_set = {1, 2, 3}
print("my set :",my_set)

# set of mixed datatypes
my_mix_set = {1.0, "Hello", (1, 2, 3)}
print("my set containing diff datatypes : ",my_mix_set)

# we can make set from a list
# Output: {1, 2, 3}
my_listset = set([1,2,3,2])
print("can convert list to set : list :",[1,2,3,2])
print("set from list",my_listset)

# add an element
# Output: {1, 2, 3}
my_set.add(7)
print("add single element to set using set.add ",my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2,3,4])


# remove element from the set using remove and discard
# remove will raise an error if element is not present in the set
print("trying to remove 5 from set using discard(5)",my_set)
my_set.discard(5)

print("trying to remove 5 from set using remove(5) will give error")
#my_set.remove(5)

# can pop an element from the set.it could be any element.
print("using pop on list ",my_listset)
print("popped eleemnt is :",my_listset.pop())

# clear my_set
#Output: set()
my_mix_set.clear()
print("using set.clear() to clear all the values " ,my_mix_set)


#union operation
print("the union of myset and my_listset :",my_set|my_listset)
#or  my_set.union(my_listset)

#intersection operation
print("the intersection of myset and my_listset :",my_set & my_listset)
#or  my_set.intersection(my_listset)

#difference operator
print("the difference of myset and my_listset :",my_set-my_listset)
#or  my_set.difference(my_listset)

#Symmetric Difference of A and B is a set of elements in both A and B except those that are common in both.
print("the Symmetric difference of myset and my_listset :",my_set^my_listset)
#or  my_set.union(my_listset)



#Frozenset is a new class that has the characteristics of a set,
# but its elements cannot be changed once assigned. While tuples are immutable lists, frozensets are immutable sets.
#Frozensets can be created using the function frozenset().

A = frozenset([1, 2, 3, 4])




































