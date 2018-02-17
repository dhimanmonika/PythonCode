
def Readfile(filename):
    list_to_return = []
    with open(filename) as f:
        line = f.readline()
        while line:
            list_to_return.append(int(line))
            line = f.readline()
    return list_to_return




list1 = Readfile('File1Overlap.txt')
list2 = Readfile('File2Overlap.txt')

overlaplist = [elem for elem in list1 if elem in list2]
print(overlaplist)
