
# here is proof and exmple refferece counting in python
# Path: Python%20Fundamental/Week1/Class-2/class2.py
import sys # import sys module
a = 10                                          # reference count of 10 is 1
print("Value of a")                             # print the value of a
print("Address  of a",id(a))                         # get the memory address of 10
print("Adrees of a  in Hexadecima form",hex(id(a)))   # get the memory address of 10 in hexadecimal
print("Reference count vlaue of 10  is ",sys.getrefcount(a))                       # get the reference count of 10 (1)
# if we assign a to b then the reference count of a will be 2 
b = a                                         # assign a to b 
print(" Now Reference count vlaue of 10  is ",sys.getrefcount(a)) 
# if we assign a to c then the reference count of a will be 3
c = a                                         # assign a to c
print(" Now Reference count vlaue of 10  is ",sys.getrefcount(a))
# if we delete a then the reference count of a will be 2 
del a                                         # delete a
print(" after del a Reference count vlaue of 10  is ",sys.getrefcount(b))
# if we delete b then the reference count of a will be 1
del b                                         # delete b
print(" after del b Reference count vlaue of 10  is ",sys.getrefcount(c))
# if we delete c then the reference count of a will be 0
del c                                         # delete c
# print(" after del c Reference count vlaue of 10  is ",sys.getrefcount(c))
# output is error because c is deleted and we are trying to access it
print("next line")
#   # using ctypes module
import ctypes
def ref_count(address):  # get the reference count of the object
    return ctypes.c_long.from_address(address).value


numbers = [1, 2, 3]
numbers_id = id(numbers)

print(ref_count(numbers_id))  # 1

ranks = numbers
print(ref_count(numbers_id))  # 2

ranks = None
print(ref_count(numbers_id))  # 1

numbers = None
print(ref_count(numbers_id))  # 0

print("next line")

# using gc module
import gc
import ctypes

def ref_count(address):  # get the reference count of the object
    return ctypes.c_long.from_address(address).value

numbers = [1, 2, 3]
numbers_id = id(numbers)

print(ref_count(numbers_id))  # 1

ranks = numbers

print(ref_count(numbers_id))  # 2

ranks = None
gc.collect() # garbage collection (gc) module is used to clean up unreferenced objects
print(ref_count(numbers_id))  # 1

numbers = None
gc.collect()
print(ref_count(numbers_id))  # 0
# Path: Python%20Fundamental/Week1/Class-2/class2.py



import gc
print(gc.isenabled()) # check if the garbage collector is enabled or not 
gc.disable() # disable the garbage collector 
print(gc.isenabled()) # check if the garbage collector is enabled or not
gc.enable() # enable the garbage collector 
print(gc.isenabled()) # check if the garbage collector is enabled or not 

# lets play with gc module
import gc
print(gc.get_count()) # get the current collection count (0,0,0)
print(gc.get_threshold()) # get the current collection threshold (700,10,10)
print(gc.get_stats()) # get the current collection stats (0,0,0)
print(gc.collect()) # collect the garbage (0)


# here gc module is used to clean up unreferenced objects
# gc.collect() # garbage collection (gc) module is used to clean up unreferenced objects
# gc.get_count() # get the current collection count (0,0,0)
# gc.get_threshold() # get the current collection threshold (700,10,10)
# gc.get_stats() # get the current collection stats (0,0,0) 
# gc.collect() # collect the garbage (0)




# proof of heap memory allocation in python
# Path: Python%20Fundamental/Week1/Class-2/class2.py


import ctypes
import gc
import sys

def ref_count(address):  # get the reference count of the object
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id):  # get the object by id
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not found"

class A:
    def __init__(self):
        self.b = B(self) 
        print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))
              
class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))
              
gc.disable()  # disable the garbage collector
my_var = A()
a_id = id(my_var)
b_id = id(my_var.b)

print(hex(a_id))
print(hex(b_id))

print(ref_count(a_id))
print(ref_count(b_id))

print(object_by_id(a_id))
print(object_by_id(b_id))

my_var = None
print(ref_count(a_id))
print(ref_count(b_id))


gc.collect()
print(ref_count(a_id))
print(ref_count(b_id))

print(object_by_id(a_id))
print(object_by_id(b_id))


# proof of stack memory allocation in python
# Path: Python%20Fundamental/Week1/Class-2/class2.py

import ctypes
import gc
import sys

def ref_count(address):  # get the reference count of the object
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id):  # get the object by id
    
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not found"

class A:
    
    def __init__(self):
        self.b = B(self) 
        print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))

class B:
      
      def __init__(self, a):
          self.a = a
          print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))

gc.disable()  # disable the garbage collector
my_var = A()
a_id = id(my_var)
b_id = id(my_var.b)

print(hex(a_id))
print(hex(b_id))

print(ref_count(a_id))
print(ref_count(b_id))

print(object_by_id(a_id))
print(object_by_id(b_id))

my_var = None
print(ref_count(a_id))
print(ref_count(b_id))











############################################################################################################
