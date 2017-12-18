"""generator to generate square of nmbers in list"""

#==============================generator as function======================================

"""def square(nums):
    for i in nums:
        yield (i*i)
        

for x in square([1,2,3,4,5,6]):
    print(x)
        
        """

#====================================One liner =============================================

square =(i*i for i in [1,2,3,4,5,6])

for x in square:
    print(x)