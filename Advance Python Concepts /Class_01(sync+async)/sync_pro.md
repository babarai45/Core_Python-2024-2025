# Here is Advance concpts of Sync and Async Programing 
--------------------------------------------------------------------

# Synce Programing :
- synce programing is technique for writing programing (espacially for function is python)
- In this teqnique function run step by step in order form 
- It is also called blocking programing 
- It is also called linear programing or linear execution or sequential programing
- It is also called Synchronous programing
  
  - ### Example
    - Here is five function :
  - fun1()     Fisrt run then go to second 
  - fun2()     
  - fun3()
  - fun4()
  - fun5()

```python
# start  

def func1():   # start here whenever it not complete it not go to for next function
    pass 

    
    
```

```python
# Second Function

def func2():   # start here whenever it not complete it not go to for next function
    pass 

```

```python 
# Third Function

def func3():   # start here whenever it not complete it not go to for next function
    pass 

```

```python

# Fourth Function

def func4():   # start here whenever it not complete it not go to for next function
    pass 

```

```python

# Fifth Function

def func5():   # start here whenever it not complete it not go to for next function
    pass 

```
### Note :
- In this programing function run step by step in order form
- It is also called blocking programing 

### Advantages :
- It is easy to understand
- It is easy to debug
- It is easy to write code
- It is easy to maintain code

### Disadvantages :
- It is slow
- It is not efficient
- It is not scalable
- It is not flexible
- It is not reliable
- It is not robust

### When to use Synce Programing :
- When we have small programing
- When we have small data
- When we have small task

### When not to use Synce Programing :
- When we have large programing
- When we have large data
- When we have large task

### Real Life Example of Synce Programing  by using Python  code :

```python
# Example of Synce Programing

import time

def task1():
    print("Task 1 start")
    time.sleep(3)
    print("Task 1 end")

def task2():
    print("Task 2 start")
    time.sleep(3)
    print("Task 2 end")

def task3():
    print("Task 3 start")
    time.sleep(3)
    print("Task 3 end")

def task4():
    print("Task 4 start")
    time.sleep(3)
    print("Task 4 end")

def task5():
    print("Task 5 start")
    time.sleep(3)
    print("Task 5 end")


if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()
    task5()

```

### Output :
```python
Task 1 start
Task 1 end
Task 2 start
Task 2 end
Task 3 start
Task 3 end
Task 4 start
Task 4 end
Task 5 start
Task 5 end
```

### Conclusion :
- In this programing function run step by step in order form
- It is also called blocking programing
- It is also called linear programing or linear execution or sequential programing

--------------------------------------------------------------------
