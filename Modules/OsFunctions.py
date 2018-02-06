"""
OS MODULE  :
"""
import os
path1="C:\\Users\\dhimam\\Desktop\\GitWork\\PythonCode"
path="C:\\Users\\dhimam\\Desktop\\ABC"
#Executing a shell command
os.system()

#Get the users environment
os.environ()

#Returns the current working directory.
os.getcwd()

#Return the real group id of the current process.
os.getgid()

#Return the current process’s user id.
os.getuid()

#Returns the real process ID of the current process.
os.getpid()

#Return information identifying the current operating system.
os.uname()

#Change the root directory of the current process to path.
os.chroot(path)

#Return a list of the entries in the directory given by path.
os.listdir(path1)

#Create a directory named path with numeric mode mode.
os.mkdir(path)

#Recursive directory creation function.
os.makedirs(path)

#Remove (delete) the file path.
os.remove(path)

#Remove directories recursively.
os.removedirs(path)

#Rename the file or directory src to dst.
os.rename(src, dst)

#Remove (delete) the directory path.
os.rmdir(path)