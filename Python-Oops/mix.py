# ---- Mix Concept Of OOPS with Different Resources ----
# ------------------------------------------------------

# What OOPs is?
# Object-oriented programming (OOP) is a programming paradigm
# based on the concept of "objects", which can contain data,
# in the form of fields (often known as attributes or properties),
# and code, in the form of procedures (often known as methods).

# what class ?
# Class is a blueprint of an object or a template of an object
# Class is a collection of objects related to each other
# (attributes and methods)
# Class Group of attributes and methods

# what is object ?
# Object is an instance of a class
# Object is a real world entity
# data + functions = object 


# Instance
# Instance is an object of a class

# Class name should be in PascalCase

# Class Consists of Members
# Members are Attributes and Methods
# Attributes are variables/fields/properties/data members
# Methods are functions/procedures/behaviors/member functions





#------------------------------------------------------------
class Product:    # Class Declaration
    pass          # Body of the class

p1 = Product()    # Obejct creation or instantiation

print(Product())  # <__main__.Product object at 0x7f8b1b3b5d30>
print(p1)         # <__main__.Product object at 0x7f8b1b3b5d30>
print(type(p1))   # <class '__main__.Product'>
print(type(Product)) # <class 'type'>
print(type(p1) == type(Product)) # False

# so p1 is named as object of class Product 
# P1 is an instance of class Product
# p1 is reference of object of class Product
#------------------------------------------------------------

class Product:    # Class Declaration
    name = 'book' # Class Variable
    price = 100   # Class Variable

p1 = Product()    # Obejct creation or instantiation
print(p1.name)    # book
print(p1.price)   # 100

p2 = Product()
print(p2.name)    # book
print(p2.price)   # 100

# so p1 and p2 are named as object of class Product
# P1 and p2 are instance of class Product
# proof
print(p1.name == p2.name) # True



#------------------------------------------------------------

# what is constructor ?
# Constructor is a special method in python
# Constructor is used to initialize the object
# Constructor is executed automatically when object is created
# Constructor is used to create instance variables
# Constructor is used to initialize instance variables

# Constructor is also known as initializer or magic method or dunder method

# Constructor is __init__() method in python 

# Constructor is used to initialize instance variables :
# self.name = pro_name
# self.name is instance variable
# pro_name is parameter of constructor

# Constructor is used to create instance variables :
# self.name is instance variable
# self.name is created by constructor

# what is instance variable ?
# Instance variable is variable which is created by constructor
# Instance variable is variable which is created by object
# Instance variable is variable which is created by self
# Instance variable is variable which is created by instance

# Example of instance variable:

# self.name = pro_name 
# here is name is instance variable 
# name is created by constructor

# self is reference of object 
# self is reference of instance


#------------------------------------------------------------

class Product:    # Class Declaration
    brand = "Apple"   # class attribute

    # constructor or initializer or magic method or dunder method
    def __init__(self, pro_name): # Constructor
        self.name = pro_name        # self.name instance attribute

    # instance method or regular method or normal method
    def display(self):             # Method
        return f'Product Name: {self.name}, Brand: {Product.brand}'
    
p1 = Product("Labtop")  # 1st instance
p2 = Product("Mobile")  # 2nd instance

print(p1.display())     # Product Name: Labtop, Brand: Apple
print(p2.display())     # Product Name: Mobile, Brand: Apple


#---------- Above code visual representation ----------------
# Product class
#     brand = "Apple"  # class attribute
#     __init__(self, pro_name)  # constructor or initializer or magic method or dunder method


class MyProduct:
    pass




