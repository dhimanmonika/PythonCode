"""
a tuple is similar to a list. The difference between the two is that we cannot change the elements
of a tuple once it is assigned whereas in a list, elements can be changed.
"""

# empty tuple
my_tuple = ()
print("my empty tuple :",my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print("tuple having mixed datatypes :",my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print("nested tuple :",my_tuple)

# tuple can be created without parentheses
# also called tuple packing
my_tuple = 3, 4.6, "dog"
print("Tuple created without paranthesis ",my_tuple)

# tuple unpacking is also possible

a, b, c = my_tuple
print("unpacking in tuple :")
print(a)
print(b)
print(c)


# only parentheses is not enough
# Output: <class 'str'>
my_tuple = ("hello")
print("my_tuple = ('hello') \n",type(my_tuple))

# need a comma at the end
# Output: <class 'tuple'>
my_tuple = ("hello",)
print("my_tuple = ('hello',)\n ",type(my_tuple))

# parentheses is optional
# Output: <class 'tuple'>
my_tuple = "hello",
print("my_tuple = 'hello', \n",type(my_tuple))


#my_tuple[1] = 9 will give error as tuple is immutable

# but item of mutable element can be changed
# Output: (4, 2, 3, [9, 5])
my_tuple1 = (4, 2, 3, [6, 5])
print("my_tuple1 ",my_tuple1)
my_tuple1[3][0] = 9
print("can change the mutable element of tuple like my_tuple[3][0] = 9  :",my_tuple1)


# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print("can repeat the elemnt using * ",("Repeat",) * 3)

my_tuple3 = ('a','p','p','l','e',)
print("my_tuple3 ",my_tuple3)
# Count
# Output: 2
print("my_tuple3.count('p') ",my_tuple3.count('p'))

# Index
# Output: 3
print("my_tuple3.index('l') ",my_tuple3.index('l'))

















