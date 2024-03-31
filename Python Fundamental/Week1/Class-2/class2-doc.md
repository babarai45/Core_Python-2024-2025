# Welcome to Class 2 
## Topics to be covered 
### 1. Python Memory Management



# Python Memory Management 
- Python memory management is the process of allocating and deallocating memory in order to optimize the use of memory.
- Python memory management is handled by Python memory manager. 
- Python memory manager is responsible for the allocation of memory and deallocation of memory.
# - main components of Python memory manager are:
# - reference counting
        - reference counting is a technique used to keep track of the number of references to an object.
        - when the reference count of an object becomes zero, the object is deallocated.
        - reference counting is a simple and efficient way to manage memory.
        - example:
        ```python
        a = 10 # reference count of 10 is 1
        b = a  # reference count of 10 is 2 
        c = a  # reference count of 10 is 3
        del a  # reference count of 10 is 2  
        del b  # reference count of 10 is 1 
        del c  # reference count of 10 is 0
        ```
        - when the reference count of an object becomes zero, the object is deallocated.
        - for detailed explanation of reference counting, see the following link:
        - https://www.pythontutorial.net/advanced-python/python-references/
        - https://www.codesansar.com/python-programming/reference-counting.htm
# proof of reference counting :
-    in python file: D:\Python_2024-25\Python Fundamental\Week1\Class-2\class2.py
# - garbage collection :
        - garbage collection is a technique used to reclaim memory that is no longer in use.
- proof of garbage collection :
```python
import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())
```

 #   - heap management :
 - heap management is the process of allocating and deallocating memory in the heap.
 - the heap is a memory pool that is used to store objects.
- - the heap is managed by the Python memory manager.
```python
import sys
print(sys.getsizeof(10))
print(sys.getsizeof(10.0))

```



#   - stack management :
- stack management is the process of allocating and deallocating memory in the stack.
- the stack is a memory pool that is used to store local variables and function calls.
- the stack is managed by the Python memory manager.
- the stack is used to store local variables and function calls.
```python
import sys
print(sys.getsizeof(10))
print(  sys.getsizeof(10.0))
```

#    - Memory Pool :
- Memory pool is a pool of memory that is used to store objects.
- Memory pool is managed by the Python memory manager.
- Memory pool is used to store objects.




