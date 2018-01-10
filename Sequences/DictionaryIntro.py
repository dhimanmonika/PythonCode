"""
Python dictionary is an unordered collection of items.
A dictionary has a key: value pair.
While values can be of any data type and can repeat, keys must be of immutable type (string, number or tuple with immutable elements)
and must be unique.
"""
# empty dictionary
my_dict = {}

print("dictionary with integer keys")
my_dict = {1: 'apple', 2: 'ball'}
print(my_dict)

print("dictionary with mixed keys")
my_mix_dict = {'name': 'John', 1: [2, 4, 3]}
print(my_mix_dict)

print("creating dictionary using dict()")
my_dict1 = dict({1:'apple', 2:'ball'})
print("dict({1:'apple', 2:'ball'})  : ",my_dict1)


#accessing values from dict
print("accessing values of my_dict(1) :",my_dict[1])

# Trying to access keys which doesn't exist throws error

# update value
print("updating the value of my dict : ")
my_dict[2] = 'bat'
print("my_dict[2] = 'bat'",my_dict)


# add item
print("add item to dictionary")
my_dict['address'] = 'Downtown'

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)


#pop item from the dictionary
print("pop elemennt using dict.pop(key) : my_dict.pop(1) :",my_dict.pop(1))
print(my_dict)

#pop arbitrary element from the dictionary
print("pop elemennt using dict.popitem() : my_dict.popitem() :",my_dict.popitem())
print(my_dict)

#remove all the elements of dictionary
print("removing all elemnts of dic using my_dict.clear() ",my_dict.clear())
print(my_dict)

# delete the dictionary itself
print("del can delete the dictionary itself  del my_dict:")
del my_dict

# check if element present in dictionary
print("check if key present in dict using in operator  1 in my_mmix_dict :" ,1 in my_mix_dict)









