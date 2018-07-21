import os

def print_directory(mpath):
    for schild in os.listdir(mpath):
        schildpath=os.path.join(mpath,schild)
        if os.path.isdir(schildpath):
            print_directory(schildpath)
        else:
            print(schildpath)
def usewalk(mpath):
    for child in os.walk(mpath):
        print(child)


if __name__ =="__main__":
    path="C:\\Users\\dhimam\\Desktop\\GitWork\\PythonCode\\OOP"
    print_directory(path)
    usewalk(path)