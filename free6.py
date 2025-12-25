#file input output : different operation read and write data
'''
Types of all files:
1. Text files: txt,.docx,.log etc.
2. Binary files: .mp4,.mov,.png,.jpeg etc.
'''
'''
f=open("file_name","mode")  mode: r:read mode and w:write mode
'''
f=open("free5.py","r")
data = f.read()
print(data)
print(type(data))
f.close()

'''
'r' = open for reading
'w' = open for writing, truncating the file first
'x' = create a new file and open it for writing
'a' = opening for writing, appending to the end of the file if it exists
'b' = binary mode
't' = text mode(default)
'+' = open a disk file for updating (reading and writing)
 data = f.read() #read entire file
 data = f.readline() # reads one line at a time

 
'''
print("......")
f=open("free5.py","r")
data = f.readline()
print(data)
f.close()
'''
writing to a file
f= open("file name","mode write")
f.write
f= open("filename","a") (a = append)
f.write
'''
f = open("day7.py","a")
f.write ("\nb=3")
f.close()

f= open("sample.py","w") #if the file doesnot exist the it create the file
f.close()

f= open("sample.py","r+")
f.write("a=123")
f.close()

'''
with syntax
with open("file name","a") as f:
data =f.read()
'''

with open("sample.py","r") as f:
    data = f.read()
    print(data)
    f.close()

with open("sample.py","w") as f:
    f.write("r=678")
    f.close()

    '''
    Deleting a file
    import os
    os.remove(filename)

    pip install tensorflow
    pip3 install tensorflow
    '''

    import os
    os.remove("sample.py") #deleting of file 