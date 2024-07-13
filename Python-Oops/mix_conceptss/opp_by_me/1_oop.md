# what is oop?
1. OOP stands for Object-Oriented Programming.
2. ways of organizing the code.
3. python supports multiple programming paradigms.
   => procedural oriented programming
   => Functional oriented programming
   => object-oriented programming

# procedural oriented programming
1. In procedural oriented programming, we write the code in the form of step by step.
2. It is a top-down approach.
3. it executes line by line.
   ## => Problems :
4. It is not easy to maintain the code.
5. It is not easy to reuse the code.
6. It is not easy to extend the code.
7. It is not easy to understand the code.
8. It is not easy to debug the code.
9.  It is not easy to test the code.

# Functional oriented programming

1. In functional oriented programming, we write the code in the form of functions.
2. It is a bottom-up approach.
3. in which we divide the code into  parts and each part is called a function and each function is responsible for a specific task
4. for this we reuse the code.
5. It is easy to reuseable the code but not solve real-world problems. 


# Object-oriented programming
1. In object-oriented programming, we write the code in the form of objects.
2. It is a real-world approach.
3. In which we divide the code into parts and each part is called an object and each object is responsible for a specific task.
4. It is easy to maintain the code.
5. It is easy to reuse the code.
6. It is easy to extend the code.
7. It is easy to understand the code.
8. It is easy to debug the code.
# important!
1. Oop is not a programming language.
2. Oop is a programming concept/way/style  to solve real-world problems.
3. Oop is a way to organize the code.
4. oop is approach to write the code in the form of classes and objects.

# Real-world example
1. In real-world, we have many objects like a pen, book, chair, table, etc.
2. Each object has two properties.
   => State/Attribute/Properties/Variable/data
   => Behavior/Method/Function/Operation/work

# why we need oop?
1. To solve real-world problems.
2. To organize the code.
3. To reuse the code.
4. To extend the code.
5. data security.
6. data hiding. 



# Class
1. A class is a blueprint/template/prototype for creating the object.
2. class is a collection of objects.
3. class is a logical entity.
4. class is common noun.
# types of class
1. Built-in class
2. User-defined class
# prof of class
1. class is a keyword in python.
2. class name should be in CamelCase.
3. class name should start with a capital letter.
4. class name should be a noun.
5. class name should not be a keyword.
6. class name should not be a built-in function.
7. class name should not be a built-in module.
8. class name should not be a built-in class.
9. class name should not be a built-in data type.
10. class name should not be a built-in method.
```python
# every thing is a class in python
x = 10
print(type(x)) # <class 'int'>

y = "hello"
print(type(y)) # <class 'str'>

z = [10, 20, 30]
print(type(z)) # <class 'list'>

# so here x, y, z are objects of int, str, list class.

#syntax of class
class ClassName:
    pass

# Example:
class Email:
    pass

# so here Email is a class.

# object of class
email = Email()
# so here email is an object of Email class.

print(type(email)) # <class '__main__.Email'>

# so here email is an object of Email class.

```
Example:
```python
class Email:
    def __init__(self, subject, message):
        self.subject = subject
        self.message = message

    def send_email(self):
        print(f"Email sent with subject: {self.subject} and message: {self.message}")
```

# Object
1. An object is an instance of a class.
2. object is a physical entity.
3. object is a real-world entity.
4. object is a proper noun.
5. Every object has two properties.
   => State/Attribute/Properties/Variable/data
   => Behavior/Method/Function/Operation/work

Example:
```python
email = Email("Hello", "How are you?")
email.send_email()

# Output
# Email sent with subject: Hello and message: How are you?

# so here  email is an object of Email class.
# Email is a class.
# email is an object.
# subject and message are the properties of the email object.

# send_email is a method of the email object.

```

#  ----------------- >         Day-4         <----------------------

