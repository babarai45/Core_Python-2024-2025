#------------- PYTHON PROGRAMING -------------#
-----------------------------------------------
Python is a high-level, interpreted, interactive
and object-oriented scripting language. 
Python is designed to be highly readable.
It uses English keywords frequently where 
as other languages use punctuation, 
and it has fewer syntactical constructions
than other languages.
Python is a MUST for students and working
professionals to become a great Software Engineer
specially when they are working in Web Development Domain.
I will cover the following topics in this course:

-----------------------------------------------
#------------- PYTHON Oop -------------#
-----------------------------------------------
    Python Object Oriented Programming
-----------------------------------------------
What is Object Oriented Programming?
Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data, in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods).
1. In object oriented programming is approach to solve the problem by creating Classes and objects.
2. In object oriented programming more focus on data rather than logic.
-----------------------------------------------

#------------Oop definition-------------#
-----------------------------------------------
1. Actually it is way of organizing the code
2. It is paradigm(نمونہ) of programming
3. In programming, a paradigm is a style or method of coding that defines a set of principles, techniques, and patterns for structuring code to solve problems on a computer.
4. It is a way of thinking about the code

Python is a multi-paradigm programming language. It supports different programming approaches.

-----------------------------------------------

1. => Procedural Programming/Imperative Programming/Structured Programming/Sequential Programming

In procedural programming, the program is built from one or more procedures or functions. Each procedure or function contains a set of instructions that are executed one after the other. It is a way of writing code where we write a set of instructions to solve the problem.
### Benefits of Procedural Programming
1. Easy to understand
2. Easy to write
3. Easy to maintain
4. Easy to debug
5. Easy to test
6. # But we can't reuse code (problem in reusability)

### Example: 
```python
length = 10               # statement 1
width = 20                # statement 2
area = length * width     # statement 3
print(area)               # statement 4

# it Runs from top to bottom and executes each statement in order that can be called procedural programming
```
-----------------------------------------------

2. => Functional Programming/Declarative Programming/Logic Programming/Constraint Programming/Modular Programming/Recursive Programming/Re-active Programming/procedure oreinted programming


# procedure oreinted programming
serie of function/instruction to complete a task

In functional programming, we use functions to solve the problem. We can use the same function multiple times in the program. It is a way of writing code where we write functions to solve the problem.
### Benefits of Functional Programming
1. Reusability
2. Easy to debug
3. Easy to test
4. Easy to understand
5. Easy to maintain
6. # But we didn't solve Real World Problems


### Example:
```python
def area(length, width):
    return length * width

print(area(10, 20)) # 200

# if i want to calculate the area of another rectangle then i can use the same function

print(area(20, 30)) # 600

# it is called functional programming
```


3. => Object Oriented Programming/Component Programming/Event-Driven Programming/Aspect-Oriented Programming/x


In object-oriented programming, we use classes and objects to solve the real-world  problem. It is a way of writing code where we write classes and objects to solve the real-world  problem.
1. In object oriented programming is approach to solve the problem by creating Classes and objects.
2. In object oriented programming more focus on data rather than logic.

### Benefits of Object Oriented Programming
1. Reusability
2. Easy to debug
3. Easy to test
4. Easy to understand
5. Easy to maintain
6. Easy to solve real-world problems
7. Easy to implement
8. Easy to manage
9. Easy to collaborate
10. Easy to secure
11. Easy to scale
12. Easy to develop

### Example:
```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

r1 = Rectangle(10, 20)
print(r1.area()) # 200

r2 = Rectangle(20, 30)
print(r2.area()) # 600

# it is called object oriented programming
```

-----------------------------------------------


#  It is most important concept :
- when we develop or design any SOF we Follow SDC principal
- SDC stand for (software development cycle) so for this 
- Best Approch/Practics we used OOPS 
- For every application (web,sof,ai app,etc..)
- main reason it is very fast real-life implementation


# ----------why we use OPPs ?
- 1- Reusability (code reuse)
- 2- Maintainability (easy to maintain)
- 3- Scalability (easy to scale) 
- 4- Security (secure code)
- 5- Flexibility (easy to change)
- 6- Understandability (easy to understand)
- 7- Testability (easy to test)
- 8- Performance (fast code)
- 9- Productivity (fast development)
- 10- Reliability (reliable code)
- 11- Modularity (easy to modularize)
- 12- Extensibility (easy to extend)
- 13- Encapsulation (secure code)
- 14- Abstraction (easy to abstract)
- 15- Polymorphism (easy to polymorph)
- 16- Inheritance (easy to inherit)

 
----------------------------------------------------------


# - 4 Pillers of OPPs 
1- Encapsulation  (data hiding) python does not support data hiding but
 we can achieve it by using private variable(custome way)

2 - Inheritance 

3 - Polymorphism 

4 - abstraction 

-----------------------------------------------------------

##  prerequest to implement above 4 piller you first knowledge
about
1- class 
2- object/instance
3- method /function
4- attribute /variable
5- constructor
6- destructor
7- class member


-------------------------------------------
OOPs is not a programming language or tool, it is a way of organizing the code/ OR guaidline to write the code
-------------------------------------------
# Example of OOPs real life
like Holy Quran is a best book in the world to spend a perfect  complete life it provide us a complete guaidline to spend a life in a good way

# Example of OOPs in programming
like we have a project and we have to write a code for that project so we have to follow the OOPs concept to write a code in a good way


-----------------------------------------------
#------------- Python Oop -------------#

# what is Object?
    An object is a real-world entity that has state and behavior.
here is below iamge:
![image](/Python-Oops/mix_conceptss/images/1.png)

    Object(شے,cheeze) is a real world entity[ہستی,body,things,item](like pen, chair, table, computer, mobile, etc) which has state and behavior.

# story telling
my house on main road and today i saw a all 
senarios from my room window
i saw some trees in park and and some people 
and some cars on the main road and some house 
on the opposite side of main road 

these are real world entities and they have 
state and behavior

if we see the tree these are different in size and 
color and they have behavior like give oxygen
and grow but it is tree

if we see the people these are different in age and
color and they have behavior like eat, walk, speak
but it is people/human

if we see the car these are different in color and
model and they have behavior like run but it is car

if we see the house these are different in size and
color and they have behavior like keep things but it is house
# first we classification the real world entities
 then we create a blueprint of these entities
1. Tree
2. People       
3. Car          
4. House  
these are common nouns (people, tree, car, house)
these are real world entities that have state and behavior

# now like we four friends from People Entity

Belong to category of  people => [1. Ali, 2. Ahmed, 3. Asad, 4. Ahsan] = These are objects of People Entity

in which Ali is a different object and Ahmed is a different object and Asad is a different object and Ahsan is a different object but all are belong to People Entity
these are called proper nouns (Ali, Ahmed, Asad, Ahsan)

# an other example
teachers is common noun
babar teachere is proper noun

![image](/Python-Oops/mix_conceptss/images/2.png)



### so these common nouns are describe proper nouns
### so these common nouns are called class and these proper nouns are called object

# more detail
1. Ali (object) is a people (class) that has state[age=20, color=white]
2. Ahmed (object) is a people (class) that has state[age=25, color=black]
3. Asad (object) is a people (class) that has state[age=30, color=brown]
4. Ahsan (object) is a people (class) that has state[age=35, color=white]

1. # here is state/attribute/variable/property of object is age and color
1.property Name  is same for all objects(like age, color)
2.property Value  is different for all objects(like 20, white, 25, black, 30, brown, 35, white)
### so we can say common noun make a class and proper noun make a object
1. common noun => class
2. proper noun => object

-----------------------------------------------
2. # here is behavior/method/function of object is eat, walk, speak(VERB)[کام کرنا,چلنا,بولنا]
   
![image](/Python-Oops/mix_conceptss/images/3.png)

1.method Name  is same for all objects(like eat, walk, speak,runing,etc..) 
2.method Value  is different for all objects(like Ali eat, Ahmed walk, Asad speak, Ahsan runing)

## what is satate and behavior here is example

# state
satae/satus/attribute/variable/property is a value of object(Ali, Ahmed, Asad, Ahsan) and its value is different for all objects(age=20, color=white, age=25, color=black, age=30, color=brown, age=35, color=white)

but why we ask attribute?
basically it is a value of object(Ali, Ahmed, Asad, Ahsan) and its value is different for all objects(age=20, color=white, age=25, color=black, age=30, color=brown, age=35, color=white) but 
in term of oop when we set a value of satate inside the class then we call it attribute.

# behavior
behavior/method/function is a action of object(Ali, Ahmed, Asad, Ahsan) and its value is different for all objects(eat, walk, speak,runing)

but why we ask method?
basically it is a action of object(Ali, Ahmed, Asad, Ahsan) and its value is different for all objects(eat, walk, speak,runing) but
in term of oop when we set a function inside the class then we call it method.

###  so state and behavior is a property of object
# state => attribute/variable/property
# behavior => method/function/VERB/action
# class => common noun/People/Tree/Car/House
# object => proper noun/Ali/Ahmed/Asad/Ahsan

### Difference between Function and Method by Table 
| Function | Method |
| --- | --- |
|1 .  Purpose of function is to perform a specific task  | Purpose of method is to perform a specific task same working both|
|2 .  Function is independent of class(common noun) | Method is dependent of class(common noun) |
|3 .  Function is not bound to a class | Method is bound to a class |
|4 .  Function call by its name | Method call by its name with object |
|5 .  Function don't require self parameter | Method require self parameter |
|6 .  Function don't require any  operator | Method require . operator for accessing objects  |

### Example:
```python
def area(length, width):     # function name is area
    return length * width
result =area(10, 20)          # function call by its name area only 
print(result)                

# here wo not need any accesser or object to call the function

but in term of method 

class Rectangle:
    def area(self, length, width):     # method name is area
        return length * width
r1 = Rectangle()                       # object creation
print(r1.area(10, 20))         # method call by its name with object r1

# here we need call the method with object r1 to access the method by using self parameter and . operator

```
### so we can say that function is a independent of class and method is dependent of class

# IN TERM OF English Example

Runnig ab ya ak action[kam ,verb ha ] hai jo koi bhi person kar sakta hai or jb bhi mery kano ma ya word sunta hai to us ka mind ma ya action a jata hai k 

Running is verb and verb is action/kam/function so that when i hear this word then i know that this is action/kam/function but idont know who is doing this action/kam/function so that is called function
because it is have only name of action/kam/function but i dont know who is doing this action/kam/ so this function it is not provide any information about to understand the action/kam/function properly sense

but when i say that Ali is running then i know that who is doing this action/kam/function so that is called method because it is have name of action/kam/function and also provide information about who is doing this action/kam/function so that is called method
here Ali is object(proper noun) and running(verb) is action/kam/function so that is called method
belnog to class people and object is Ali

```python
def running():     # function name is running
    print("i don't know who is doing this action")
running()          # function call by its name running only
 but 
class People:
    def running(self):     # method name is running
        print("Ali is doing this action")
Ali = People()             # object creation
Ali.running()              # method call by its name with object Ali
```

### so we can say that function is a independent of class and method is dependent of class

-----------------------------------------------

# Difference between Variable and Attribute by Table
| Variable | Attribute |
| --- | --- |
|1 .  Variable is a name of state | Attribute is a name of state inside the class |
|2 .  Variable is a name of memory location | Attribute is a name of memory location inside the class |
|3 .  Variable is a name of container | Attribute is a name of container inside the class |
|4 .  Variable is a independent of class | Attribute is a dependent of class |
|5 .  Variable don't  need any accesser to print the value | Attribute need . operator to print the value |
|6 .  Variable is a name of data | Attribute is a name of data inside the class |

### Example:
```python
length = 10               # variable name is length
width = 20                # variable name is width
area = length * width     # variable name is area

print(area)               # variable print by its name area only

but in term of attribute

class Rectangle:
    length = 10           # attribute name is length
    width = 20            # attribute name is width
    area = length * width # attribute name is area

r1 = Rectangle()          # object creation
print(r1.area)            # attribute print by using . operator with object r1


```
### so we can say that variable is a independent of class and attribute is dependent of class

-----------------------------------------------
# In term of English Example

color is white  is a name of state/status and it is a variable because it is a name of state
color = white
but i don't know who is white so it is a variable because it is a name and its value is white only
whitle color could be anything but i don't know who is white so it is a called  variable

but
Ali color is white is a name of state/status and it is a attribute because it is a name of state inside the class
Ali.color = white 
Ali is a object and white is a color so it is a attribute because it is a name of state inside the class
Ali color could be anything but i know who is white so it is a called  attribute

```python
color = "white"               # variable name is color
print(color)                  # variable print by its name color only

but in term of attribute

class People:
    color = "white"           # attribute name is color
Ali = People()                # object creation
print(Ali.color)              # attribute print by using . operator with object Ali

```
### so we can say that variable is a independent of class and attribute is dependent of class

-----------------------------------------------

# what is Class?
    A class is common noun 
    It is classifiction of real world entities(people, tree, car, house)
    A class is a blueprint(خاکہ بنانا, تصویر بنانا,design) for the object.
    A class is a template(لوہے یا مٹی کا سانچہ جس میں چیزیں ڈھالی جاتی ہیں) for the object.
    A class is a collection of objects(people, tree, car, house).
    A class is a logical entity(منطقی وجود).
    A class is a user-defined data type(استعمال کنندہ کی تعریف کی گئی ڈیٹا قسم).
    A class is a reference data type.
    => A Class is a classification of objects.
    => A Class is a group of objects that have common properties.
    => A Class is a community Name of objects.
common noun: [doctor, teacher, student, car, tree, animal, human, etc]

    
Example:
    - Class: Pen
    - Object: Blue Pen, Red Pen, Green Pen, etc.
    - Class: Chair
    - Object: Wooden Chair, Plastic Chair, Iron Chair, etc.
    - Class: Table
    - Object: Wooden Table, Plastic Table, Iron Table, etc.
    - Class: Computer
    - Object: Dell Computer, HP Computer, Lenovo Computer, etc.
    - Class: Mobile
    - Object: Samsung Mobile, Nokia Mobile, iPhone Mobile, etc.
    - etc.
  - In the world each and everything is an object.
    - Class: Human
    - Object: Ali, Ahmed, Asad, etc.
    - Class: Animal
    - Object: Dog, Cat, Lion, etc.
    - Class: Plant
    - Object: Mango Tree, Apple Tree, etc.
    - etc.
    - In programming, an object is a container that contains data and methods.
    - An object is a collection of data and methods.
    - An object is an instance of a class.



# Defining a Class
    => A class is defined using the class keyword.
    => A class is defined using the class keyword followed by the class name.
    => A class name should start with an uppercase letter.

Syntax:
    class ClassName:
        # class body

```python
# Example:
class Pen:     # class definition   
    pass
```
-----------------------------------------------

# what is Object?
    An object is proper noun
    It is object of real world entities(Ali, Ahmed, Asad, Ahsan)
    An object is a instance(نمونہ,مثال, واقعہ,special object,unique object) of the class.
    An object is a real-world entity.
    An object is a physical entity.
    An object is a reference of the class.
    An object is a reference data type.
    => An Object is a Proper Noun(Specific name) that represents a single entity.
    => An Object is a real-world entity that has state and behavior.
    => An Object is an instance of a class.
    => An Object is a collection of data and methods.
    => An Object is a container that contains data and methods.
proper noun: [doctor ali, teacher ahmed, student asad, car honda, tree mango, animal lion, human ali, etc]


# Creating an Object
    => An object is created using the class name followed by parentheses.

Syntax:
    object_name = ClassName()

```python
# Example:
p1 = Pen()
```

  
# State 
    => set of properties,value,attributes,variables,fields,characteristics,features, that are stored in an object.
    1. methods: write, refill, cap_on, cap_off
    2. attributes: color, ink, brand



# over all oop definition
1.    Object-oriented programming (OOP) is a programming paradigm that a provides a means of           
structuring programs so that properties and behaviors are bundled into individual objects.
    so python support oop concept
2.   This approach resolves arround the object
3.   object is  group of data and function/properites and methods
4.   oject is also called instance of class
5.   object is also capable of storing data and performing operations on that data such action may change the state of the object
6.   

# what is Class and Object in term of English Example
class is a common noun and object is a proper noun
class is a blueprint and object is a instance of class
class is a template and object is a reference of class
class is a collection of objects and object is a real-world entity

# what is Class and Object in term of Real World Example
class is a people and object is a Ali
class is a tree and object is a neem
class is a car and object is a honda
class is a house and object is a babar house

