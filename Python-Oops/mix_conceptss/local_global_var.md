# ------------------- Local and Global Variables 
# Local Variables:
 A variable declared inside the function's body is called a local variable.
    A local variable can only be used inside the function where it is declared.
    They are not accessible from outside the function.
    You can access the local variable only within the function in which it is declared.
    You can't access the local variable outside the function.
```python
def myfunc():
    x = 300     # local variable
    print(x)
print(myfunc())

# Output: 300


```

