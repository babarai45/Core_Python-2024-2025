# what is constructor in python? 


class  A:
    Ali = 34
    def __init__(self):
        print("I am constructor")
        print("I am called automatically when object is created")
a=A()
print(a.Ali)   #  a is object of class A and Ali is class variable
print(A.Ali)   #  A is class name and Ali is class variable

# Output:
# I am constructor
# I am called automatically when object is created
# 34
# 34


# In the above example, we have created a class A with a constructor __init__().
# The constructor is automatically called when an object of the class is created.


# Constructor with parameters
# A constructor can be defined with parameters. The parameters are passed when the object is created.

class  B:
    Babar = 'BABAR'
    def __init__(self, name, age):
        self.name = name    # name is instance variable
        self.age = age      # age is instance variable
        print("inside class A constructor", self.name, self.age)
b=B('Ali', 23)
print(b.name)
print(b.age)

# what is instance varable ?
# Ans: instance variable is a variable which is defined inside constructor with self keyword.
# In the above example, we have created a class B with a constructor __init__(self, name, age).
# The constructor is automatically called when an object of the class is created.
# The parameters name and age are passed when the object is created.
# The name and age are instance variables. They are accessed using the object of the class.

