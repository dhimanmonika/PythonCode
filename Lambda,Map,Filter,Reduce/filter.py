""" The filter() function in Python takes in a function and a list as arguments.

The function is called with all the items in the list and a new list is returned which contains items for which the function evaluats to True."""

#print only even numbers from the list

l=[1,2,6,3,4,9,7,23,66]
print("original list ",l)

#print only even numbers from the list

even=list(filter(lambda x: (x%2==0),l))
print("even numbers are:" ,even)


#print only prime numbers

def prime(n):
    if n==2:
        return True
    if n>2:
        hlf=int(n/2)
        for i in range(2,hlf+1):
            if (n%i==0):
                return False
    return True


prm=list(filter(lambda x:prime(x),l))
print("prime numbers are :" ,prm)