import os
f=open('demo.txt',"rb")
data=f.read()   # read the entire file


# data=f.read(5)  ---> it will read only initial 5 characters
# data=f.readline()  ---> read one line at a time


print(data)
print(type(data))
f.close()

# r ---> open for reading(default)
# w ---> open for writing,truncating the file first
# x ---> create a new file and open it for writing
# a ---> open for writing, appending to the end of the file if it exists
# b ---> open in binary mode
# t ---> open in text mode(default)
# + ---> open a disk file for updating (reading and writing)


# writing to a file

ff=open('demo.txt',"w")
ff.write("i want to learn js tomorrow")
ff.close()

ff=open('demo.txt',"a")
ff.write("\nthen i will move to react js")
ff.close()


ff=open('sample.txt',"w")  # if file does not exist then python will create it automatically
ff.write("i want to learn js tomorrow")
ff.close()


# reading and writing simultaneously

c=open('sample.txt','r+')
c.write("abc")
print(c.read())
c.close()


c=open('sample.txt','w+')
c.write("abc")
print(c.read())
c.close()


c=open('sample.txt','a+')
c.write("abc")
print(c.read())
c.close()

#  with syntax 

with open("demo.txt","r") as f:
      data=f.read()
      print(data)


with open("demo.txt","w") as f:
      data=f.write("hello baby")
      print(data)
      
# deleting python
# for deleting a file we need a module named as os module

os.remove("demo.txt")

