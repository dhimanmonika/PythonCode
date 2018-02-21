import os
from datetime import datetime

# to get list of available methods within module

print("functions available in os module  :", dir(os))


# to get present working dir

print("\n present working directory :",os.getcwd())


# to change dir
#os.chdir('C:\Users\dhimam\Desktop\GitWork\PythonCode\Logging')

#to get list of dirs available
print("dirs available in at cwd are :",os.listdir(os.getcwd()))


# to make dir
os.mkdir('dirMkdir')

#to make nested dirs
os.makedirs('dir1/subdir2')

#to remove dir
#os.rmdir('dir1')

# to remove directories
os.removedirs('dir1/subdir2')

#to rename

os.rename('dirMkdir','dirRename')
os.rmdir('dirRename')


#to get stats of file

print("file stats :",os.stat('calc.py'))


#to get modified time of file

modtime=os.stat('calc.py').st_mtime
print("file modified at : ",datetime.fromtimestamp(modtime))



# to get directories and subdirs from top to bottom in speecified path

for dirpath,dirnames,filename in os.walk(os.getcwd()):
    print("current path :",dirpath)
    print("directory name :",dirnames)
    print("filenames :",filename)
    print()


#to get environment variable path

print(" HOME env variable at :",os.environ.get('HOME'))

# to concat to paths using os.path
filepath = os.path.join(os.getcwd(),'calc.py')
print("path for file calc.py :",filepath)

#to get file name only(basename)
basename=os.path.basename(filepath)
print("basename for the path ",filepath,"is ",basename)


#to split path
print("parts of path after split : ",os.path.split(filepath))


#to check if path really exists
print("checking if path ",filepath ,"really exists" , os.path.exists(filepath))

#to split the extension of file from path

print(" the extension of file calc.py is :",os.path.splitext(filepath))
































