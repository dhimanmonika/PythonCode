def WriteToFile(data):
    with open('abcd.txt','w') as open_file :
        open_file.write(data)


def ReadFile(filename):
    with open(filename,'r') as my_file:
        for line in my_file:
            print(line.split())




data ="this is simple code to write a text file"
WriteToFile(data)
print("done writing")
ReadFile('abcd.txt')
print("done reading ")



