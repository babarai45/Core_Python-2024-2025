# It is week2 of our python Data structure course. We are going to learn about fils.
# We are going to learn about how to read and write files in python.

# what is a file?
# A file is a container in a computer system for storing information.

# There are two types of files:
# 1. Text file: A file that contains only printable characters and a few control characters
#  such as new line, tab, etc.
# e.g. .txt, .csv, .html, .xml, .json, etc.
# 2. Binary file: A file that contains binary data.
# e.g. .jpg, .mp3, .mp4, .exe, .pdf, etc.

# File operations:
# 1. Open a file
# 2. Read or write a file
# 3. Close a file
# 4. Delete a file
# 5. Rename a file
# 6. Check if a file exists
# 7. Get file information
# 8. Get file size
# 9. Get file modification time
# 10. Get file access time
# 11. Get file creation time
# 12. Get file permissions
# 13. Change file permissions
# 14. Change file owner
# 15. Change file group
# 16. Change file timestamps
# 17. Change file name
# 18. Change file location
# 19. Change file content
# 20. Change file size
# 21. Change file type
# 22. Change file format
# 23. Change file encoding
# 24. Change file structure
# 25. Change file metadata
# 26. Change file attributes
# 27. Change file security
# 28. files scanning
# 29. files searching
# 30. files sorting
# 31. files filtering
# 32. files grouping
# 33. files merging
# 34. files splitting
# 35. files compressing
# 36. files decompressing
# 37. files encrypting
# 38. files decrypting
# 39. files hashing
# 40. files checksumming
# 41. files comparing
# 42. files copying
# 43. files moving

# File modes:
# 1. r: read mode
# 2. w: write mode
# 3. a: append mode
# 4. r+: read and write mode
# 5. w+: write and read mode
# 6. a+: append and read mode
# 7. rb: read binary mode
# 8. wb: write binary mode
# 9. ab: append binary mode
# 10. rb+: read and write binary mode
# 11. wb+: write and read binary mode
# 12. ab+: append and read binary mode

# File handling:
# 1. Open a file
# 2. Read or write a file
# 3. Close a file

# Open a file:
# file = open('file_name', 'mode')
# file = open('file_name', 'mode', buffering)
# file = open('file_name', 'mode', buffering, encoding)
# file = open('file_name', 'mode', buffering, encoding, errors)
# file = open('file_name', 'mode', buffering, encoding, errors, newline)
# file = open('file_name', 'mode', buffering, encoding, errors, newline, closefd)
# file = open('file_name', 'mode', buffering, encoding, errors, newline, closefd, opener)

# Read or write a file:
# file.read(size)
# file.readline(size)   
# file.readlines(sizehint)
# file.write(string)
# file.writelines(lines)

# Close a file:
# file.close()

# Delete a file:
# os.remove('file_name')

# Rename a file:
# os.rename('old_file_name', 'new_file_name')

# Check if a file exists:
# os.path.exists('file_name')

# Get file information:
# os.stat('file_name')

# Get file size:
# os.path.getsize('file_name')

# Get file modification time:
# os.path.getmtime('file_name')

# Get file access time:
# os.path.getatime('file_name')

# Get file creation time:
# os.path.getctime('file_name')

# Get file permissions:
# os.stat('file_name').st_mode

# Change file permissions:
# os.chmod('file_name', mode)

# Change file owner:
# os.chown('file_name', uid, gid)

# Change file group:
# os.chown('file_name', -1, gid)

# Change file timestamps:
# os.utime('file_name', (atime, mtime))

# Change file name:
# os.rename('old_file_name', 'new_file_name')

# Change file location:
# shutil.move('old_file_name', 'new_file_name')

# Change file content:
# file = open('file_name', 'w')
# file.write('new_content')
# file.close()

# Change file size:
# file = open('file_name', 'w')
# file.truncate(size)
# file.close()

# Change file type:
# os.rename('file_name', 'file_name.new_extension')

# Change file format:
# os.rename('file_name', 'file_name.new_format')

# Change file encoding:
# file = open('file_name', 'r', encoding='old_encoding')
# content = file.read()
# file.close()
# file = open('file_name', 'w', encoding='new_encoding')
# file.write(content)
# file.close()

# Change file structure:
# file = open('file_name', 'r')
# content = file.read()
# file.close()
# file = open('file_name', 'w')
# file.write('new_structure')
# file.close()



# Change file metadata:
# os.utime('file_name', (atime, mtime))
# os.chmod('file_name', mode)
# os.chown('file_name', uid, gid)

# Change file attributes:
# os.chmod('file_name', mode)
# os.chown('file_name', uid, gid)

# Change file security:
# os.chmod('file_name', mode)
# os.chown('file_name', uid, gid)

# Files scanning:
# os.scandir('directory_name')

# Files searching:
# os.walk('directory_name')

# Files sorting:
# os.listdir('directory_name')

# Files filtering:
# os.listdir('directory_name')

# Files grouping:
# os.listdir('directory_name')

# Files merging:
# file1 = open('file1', 'r')
# content1 = file1.read()
# file1.close()
# file2 = open('file2', 'r')
# content2 = file2.read()
# file2.close()
# file = open('file', 'w')
# file.write(content1 + content2)
# file.close()

# Files splitting:
# file = open('file', 'r')
# content = file.read()
# file.close()
# file1 = open('file1', 'w')
# file1.write(content[:size1])
# file1.close()
# file2 = open('file2', 'w')
# file2.write(content[size1:])
# file2.close()

# Files compressing:
# import gzip
# file = open('file', 'rb')
# content = file.read()
# file.close()
# file = gzip.open('file.gz', 'wb')
# file.write(content)
# file.close()

# Files decompressing:
# import gzip
# file = gzip.open('file.gz', 'rb')
# content = file.read()
# file.close()
# file = open('file', 'wb')
# file.write(content)
# file.close()

# Files encrypting:
# import cryptography
# file = open('file', 'rb')
# content = file.read()
# file.close()
# file = open('file', 'wb')
# file.write(cryptography.encrypt(content))
# file.close()

# Files decrypting:
# import cryptography
# file = open('file', 'rb')
# content = file.read()
# file.close()
# file = open('file', 'wb')
# file.write(cryptography.decrypt(content))
# file.close()

# Files hashing:
# import hashlib
# file = open('file', 'rb')
# content = file.read()

# Files checksumming:
# import hashlib
# file = open('file', 'rb')
# content = file.read()
# file.close()

# Files comparing:
# file1 = open('file1', 'rb')
# content1 = file1.read()
# file1.close()
# file2 = open('file2', 'rb')
# content2 = file2.read()
# file2.close()

# Files copying:
# file1 = open('file1', 'rb')
# content1 = file1.read()
# file1.close()
# file2 = open('file2', 'wb')
# file2.write(content1)
# file2.close()

# Files moving:
# file1 = open('file1', 'rb')
# content1 = file1.read()
# file1.close()
# file2 = open('file2', 'wb')
# file2.write(content1)
# file2.close()
# os.remove('file1')
# --------------------------------------------------------------Example-------------------------------------------------------------->
# Example with live code:

# Open a file: # method1
# file=open('bar.txt', 'r')
# print(file)
# output:

# <_io.TextIOWrapper name='bar.txt' mode='r' encoding='cp1252'>
# here <_io.TextIOWrapper> is the file object.
# name='bar.txt' is the file name.
# mode='r' is the file mode.
# encoding='cp1252' is the file encoding.(optional)

# file=open('bar.txt') # method2
# for line in file: # read the first line a 
#     print(line) # output: a
# # output:

# method3
# file=open('bar.txt')  # read the first line a
# content=file.read() # here content is a string and using read() method we can read the content of the file and store it in a content  variable.
# print(content) # show the content of the file
# # # output:

# method4
# file=open('bar.txt') # read the first line a
# content=file.readlines() # here content is a list and using readlines() method we can read the content of the file and store it in a content  variable.
# # but readlines() method read the content of the file line by line and store it in a list.
# print(content) # show the content of the file in a list
# # output:

# by index and slicing methods 
file=open('bar.txt') # read the first line a
content=file.read() # here content is a string and using read() method we can read the content of the file and store it in a content  variable.
print(content[0]) # using index method we can read the content of the file by index.one by one character
print(content[0:3]) # by slicing method we can read the content of the file according to your requirement.
print(content[-10]) # using negative index method we can read the content of the file by index.one by one character
print(content[-20:]) # by slicing method we can read the content of the file according to your requirement.

# if we count  lines  method 1
file=open('bar.txt') # read the first line a
count=0
for line in file:
    count+=1
print(count) # output: 11

# if we count  lines  method 2
file=open('bar.txt') # read the first line a
content=file.readlines()
print(len(content)) # output: 11


file=open('bar.txt') # read the first line a
content=file.read()
print(len(content)) # output: 252

# and we can count the number of words in a file
file=open('bar.txt') # read the first line a
content=file.read()
words=content.split() # split the content of the file by space and store it in a list(words)
print(len(words)) # output: 11

# file=open('bar.txt') # read the first line a
# content=file.read()
# print(content[:-20])    # output: a


# file=open('bar.txt') # read the first line a
# for line in file:
#     if line.startswith('i'):
#         print(line) 
# output: i am a student.
#         i am a teacher.
file=open('bar.txt') # read the first line a
for line in file:
    if line.rstrip(): # rstip() method remove the white space from the right side of the string.
        if not line.startswith('i'): # if the line does not start with i then print the line.
            print(line)
# 042351719023
# 03287576162
# # read file content line by line :methode1
# content=file.readline() # read the first line a
# for line in content:
#     print(line) # output: character by character
# # read file content  by index :methode2
# content=file.readlines() # read the first line a
# for line in content:
#     print(line[0]) # output: character by character

# # Read file content: 
# content=file.read()
# print(content)
# # output:



fruit = 'Banana'
fruit[0] = 'b'
print(fruit)