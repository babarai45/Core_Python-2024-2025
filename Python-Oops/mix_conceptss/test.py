# def area(length, width):     # function name is area
#     return length * width
# result =area(10, 20)                 # function call by its name area only 
# print(result)

# # here we can see that we are calling the function by its name only
# # here wo not need any accesser or object to call the function

# # but in term of method 

# class Rectangle:
#     def m1(self ,l,w):
#         return l*w
# t=Rectangle()
# print(t.m1(30,20))

# # here we can see that we are calling the method by its name with object
# # here we need object to call the method

# # so the main difference between function and method is that
# # function can be called by its name only
# # method can be called by its name with object using dot operator

# # so in python we can say that method is a function which is defined inside the class
# # and it is called by its name with object using dot operator


# # so in python we can say that method is a function which is defined inside the class

# class Test:
#     def m1(self ,l,w):
#         return l*w
# t=Test()
# print(t.m1(10,20))
# new=t.m1(5,20)
# print(new)


# --------------------------------------------------------------------------------
length = 10               # variable name is length
width = 20                # variable name is width
area = length * width     # variable name is area

print(area)               # variable print by its name area only



class Rectangle:
    length = 30           # attribute name is length
    width = 20            # attribute name is width
    area = length * width # attribute name is area

r1 = Rectangle()          # object creation
print(r1.area)            # attribute print by using . operator with object r1
