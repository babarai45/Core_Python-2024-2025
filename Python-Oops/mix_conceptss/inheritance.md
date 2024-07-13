
# BY GITHUB-COPILOT
# -------------- Inheritacance ------------>
inheritance mean to extend class 


# why we use inheritance
1. Reusability of code
2. Method Overriding
3. Polymorphism
4. Data Hiding
5. Code Reusability
6. Code Organization

# imp 
1.=> Inheritance is a mechanism in which one class acquires the property of another class.
2.=> The class which inherits the properties of other is known as subclass (derived class, child class) and the class whose properties are inherited is known as superclass (base class, parent class).
3.=> Inheritance represents the IS-A relationship which is also known as a parent-child relationship.
4.=> It is used for code reusability and method overriding.
5.=> Inheritance is a powerful feature of OOP that allows the properties of one class to be used in another class.
6.=> private member of the parent class can not be accessed in the child class.
7.=> AND constructor of the parent class is never extended to the child class although the constructor of the parent class is called in the child class(through super() method).


# -------------- Types of Inheritance ------------>

1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance
6. Cyclic Inheritance

# -------------- Single Inheritance ------------>

Single inheritance is a type of inheritance in which a class inherits from only one class.

# Example
```python
class Parent:                  # Parent class
    def show(self):            # Parent class method
        print("Parent class method")            

class Child(Parent):           # Child class inheriting with Parent class
    def display(self):         # Child class method
        print("Child class method")

obj = Child()                  # Object of Child class
obj.display()                  # Child class method
obj.show()                     # Parent class method
```


# -------------- Multiple Inheritance ------------>

Multiple inheritance is a type of inheritance in which a class inherits from more than one class.

# Example
```python
class Parent1:                  # Parent1 class
    def show1(self):            # Parent1 class method
        print("Parent1 class method")

class Parent2:                  # Parent2 class
    def show2(self):            # Parent2 class method
        print("Parent2 class method")

class Child(Parent1, Parent2):  # Child class inheriting with Parent1 and Parent2 class
    def display(self):          # Child class method
        print("Child class method")

obj = Child()                   # Object of Child class
obj.display()                   # Child class method
obj.show1()                     # Parent1 class method
obj.show2()                     # Parent2 class method
```





# -------------- Multilevel Inheritance ------------>

Multilevel inheritance is a type of inheritance in which a class inherits from another class, and that class inherits from another class.

# Example
```python
class GrandParent:                  # GrandParent class
    def show1(self):                # GrandParent class method
        print("GrandParent class method")

class Parent(GrandParent):          # Parent class inheriting with GrandParent class
    def show2(self):                # Parent class method
        print("Parent class method")

class Child(Parent):                # Child class inheriting with Parent class
    def display(self):              # Child class method
        print("Child class method")

obj = Child()                    # Object of Child class
obj.display()                    # Child class method
obj.show1()                      # GrandParent class method
obj.show2()                      # Parent class method
```

# -------------- Hierarchical Inheritance ------------>

Hierarchical inheritance is a type of inheritance in which more than one class inherits from a single class.

# Example
```python

class Parent:                  # Parent class
    def show(self):            # Parent class method
        print("Parent class method")

class Child1(Parent):          # Child1 class inheriting with Parent class
    def display1(self):        # Child1 class method
        print("Child1 class method")

class Child2(Parent):          # Child2 class inheriting with Parent class
    def display2(self):        # Child2 class method
        print("Child2 class method")

obj1 = Child1()                # Object of Child1 class
obj1.display1()                # Child1 class method
obj1.show()                    # Parent class method

obj2 = Child2()                # Object of Child2 class
obj2.display2()                 # Child2 class method

```


# -------------- Hybrid Inheritance ------------>

Hybrid inheritance is a combination of two or more types of inheritance.

# Example
```python
class Parent1:                  # Parent1 class
    def show1(self):            # Parent1 class method
        print("Parent1 class method")

class Parent2:                  # Parent2 class
    def show2(self):            # Parent2 class method
        print("Parent2 class method")

class Child1(Parent1):           # Child1 class inheriting with Parent1 class
    def display1(self):         # Child1 class method
        print("Child1 class method")

class Child2(Parent2):           # Child2 class inheriting with Parent2 class
    def display2(self):         # Child2 class method
        print("Child2 class method")

class Child3(Child1, Child2):    # Child3 class inheriting with Child1 and Child2 class
    def display3(self):          # Child3 class method
        print("Child3 class method")

obj = Child3()                   # Object of Child3 class
obj.display1()                   # Child1 class method
obj.display2()                   # Child2 class method
obj.display3()                   # Child3 class method
obj.show1()                      # Parent1 class method
obj.show2()                      # Parent2 class method

# the output of the above code will be:
# Child1 class method
# Child2 class method
# Child3 class method
# Parent1 class method

so it is clear that the Child3 class is inheriting the properties of Child1, Child2, Parent1, and Parent2 class that is why it is called hybrid inheritance.
hybrid inheritance means a combination of two or more types of inheritance(like single, multiple, multilevel, hierarchical inheritance).
```


# -------------- Cyclic Inheritance ------------>   

Cyclic inheritance is a type of inheritance in which a class inherits from itself.

# Example
```python
class A(A):                  # Class A inheriting with itself
    def show(self):          # Class A method
        print("Class A method")

obj = A()                    # Object of Class A
obj.show()                   # Class A method

# the output of the above code will be:
# Class A method

so it is clear that the class A is inheriting the properties of itself that is why it is called cyclic inheritance.
cyclic inheritance means a class inherits from itself because it is not possible in python.
```


# -------------- Method Overriding ------------>

Method overriding is a feature of OOP that allows a subclass to provide a specific implementation of a method that is already provided by its superclass.

# Example
```python
class Parent:                  # Parent class
    def show(self):            # Parent class method
        print("Parent class method")

class Child(Parent):           # Child class inheriting with Parent class
    def show(self):            # Child class method
        print("Child class method")

obj = Child()                  # Object of Child class
obj.show()                     # Child class method

# the output of the above code will be:
# Child class method

so it is clear that the show() method of the Parent class is overridden by the show() method of the Child class because the Child class is inheriting the Parent class and providing its own implementation of the show() method that is why it is called method overriding.

```

# -------------- super() method ------------>

super() method is used to call the constructor of the parent class in the child class.

syntax:
super().__init__() # calling the constructor of the parent class in the child class.


# Example
```python
class Parent:                  # Parent class
    def __init__(self):        # Parent class constructor
        print("Parent class constructor")

class Child(Parent):           # Child class inheriting with Parent class
    def __init__(self):        # Child class constructor
        super().__init__()     # calling the constructor of the Parent class
        print("Child class constructor")
# but why we need to call the constructor of the parent class in the child class?
# because the constructor of the parent class is never extended to the child class although the constructor of the parent class is called in the child class(through super() method).

obj = Child()                  # Object of Child class

# the output of the above code will be:
# Parent class constructor
# Child class constructor

so it is clear that the constructor of the Parent class is called in the Child class through the super() method that is why it is called super() method.
```

# -------------- Accessing Parent Class Method ------------>

A child class can access the methods of the parent class by using the super() method.

# Example
```python

class Parent:                  # Parent class
    def show(self):            # Parent class method
        print("Parent class method")

class Child(Parent):           # Child class inheriting with Parent class
    def display(self):         # Child class method
        super().show()         # calling the show() method of the Parent class
        print("Child class method")

obj = Child()                  # Object of Child class
obj.display()                  # Child class method

# the output of the above code will be:
# Parent class method
# Child class method

so it is clear that the Child class is accessing the show() method of the Parent class by using the super() method that is why it is called accessing parent class method.
```

# -------------- Accessing Parent Class Variable ------------>

A child class can access the variables of the parent class by using the super() method.

# Example
```python
class Parent:                  # Parent class
    a = 10                    # Parent class variable

class Child(Parent):           # Child class inheriting with Parent class
    def display(self):         
        print(super().a)       # accessing the Parent class variable

obj = Child()                  # Object of Child class

obj.display()                  # 10

so it is clear that the Child class is accessing the variable of the Parent class by using the super() method that is why it is called accessing parent class variable.
```

# -------------- Accessing Parent Class Constructor ------------>

A child class can access the constructor of the parent class by using the super() method.

# Example
```python
class Parent:                  # Parent class
    def __init__(self):        # Parent class constructor
        print("Parent class constructor")

class Child(Parent):           # Child class inheriting with Parent class

    def __init__(self):        # Child class constructor
        super().__init__()     # calling the constructor of the Parent class
        print("Child class constructor")

obj = Child()                  # Object of Child class

# the output of the above code will be:
# Parent class constructor
# Child class constructor

```

# -------------- Accessing Parent Class Method and Variable using self ------------>

A child class can access the methods and variables of the parent class by using the self keyword.

# Example
```python
class Parent:                  # Parent class
    a = 10                    # Parent class variable
    def show(self):            # Parent class method
        print("Parent class method")

class Child(Parent):           # Child class inheriting with Parent class
    def display(self):         
        print(self.a)          # accessing the Parent class variable
        self.show()            # accessing the Parent class method

obj = Child()                  # Object of Child class

obj.display()          

# the output of the above code will be:
# 10
# Parent class method

so it is clear that the Child class is accessing the variable and method of the Parent class by using the self keyword that is why it is called accessing parent class method and variable using self.
```



#  =============================================================


# BY POFESSOR RIZWAN SAAB:

# Inheritance
Inheritance is a mechanism in which one class acquires the property of another class. The class which inherits the properties of other is known as subclass (derived class, child class) and the class whose properties are inherited is known as superclass (base class, parent class). Inheritance represents the IS-A relationship which is also known as a parent-child relationship. It is used for code reusability and method overriding. Inheritance is a powerful feature of OOP that allows the properties of one class to be used in another class. private member of the parent class can not be accessed in the child class. AND constructor of the parent class is never extended to the child class although the constructor of the parent class is called in the child class(through super() method).

## simple defination:
Inheritance is a mechanism in which one class acquires the property of another class.

## Why we use Inheritance
1. Reusability of code
2. Method Overriding
3. Polymorphism
4. Data Hiding
# Types of Inheritance
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance



# Single Inheritance
Single inheritance is a type of inheritance in which a class inherits from only one class.

# Example
```python
class A:
    pass
class B(A):
    pass
```

# Multiple Inheritance
Multiple inheritance is a type of inheritance in which a class inherits from more than one class.

# Example
```python
class A:
    pass
class B:
    pass
class C(A, B):          # C class inheriting with A and B class that is why it is called multiple inheritance
    pass
```

# Multilevel Inheritance

Multilevel inheritance is a type of inheritance in which a class inherits from another class, and that class inherits from another class.

# Example
```python
class A:
    pass
class B(A):
    pass
class C(B):          # C class inheriting with B class that is inheriting with A class that is why it is called multilevel inheritance
    pass
```

# Hierarchical Inheritance
Hierarchical inheritance is a type of inheritance in which more than one class inherits from a single class.

# Example
```python
class A:
    pass
class B(A):
    pass
class C(A):          # B and C class inheriting with A class that is why it is called hierarchical inheritance
    pass
```

# Hybrid Inheritance
Hybrid inheritance is a combination of two or more types of inheritance.

# Example
```python
class A:
    pass
class B:
    pass
class C(A, B):          # C class inheriting with A and B class that is why it is called hybrid inheritance
    pass
class D(C):
    pass
```

