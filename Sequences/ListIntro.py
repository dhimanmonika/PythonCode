# empty list
my_list=[]

#list of mixed datatypes
my_list1 =[1,2,"hello",7,"rr",6,9,3]
print("list of mixed datatypes ",my_list1)

#nested list
my_list2=[1,[1,2,3,4],['a']]
print("nested list :",my_list2)

# accessing elements of list
print(my_list1[2],"is the element of the my_list1 ")

# elements 3rd to 5th
print("elements of my_list1 from 3 to 5 ",my_list1[2:5])

#We can add one item to a list using append()
print("mylist2 before append ",my_list2)
my_list2.append(8)
print("after append(8)",my_list2)

#add several items using extend() method
print("mylist2 before extend ",my_list2)
my_list2.extend([4,5,6])
print("after extend([4,5,6]) ", my_list2)

#pop()
print("mylist_1 :",my_list1)
print("pop element of list1 ",my_list1.pop())


#remove()
print("mylist2 before remove ",my_list1)
my_list1.remove(2)
print("after remove(2)",my_list1)




