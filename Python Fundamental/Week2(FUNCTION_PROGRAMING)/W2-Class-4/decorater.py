# python Decorator is a function 
# that takes another function and extends the 
# behavior of the latter function without explicitly modifying it.
# Decorators provide a simple syntax for calling higher-order functions.
# Decorators are a powerful tool in Python, since it allows programmers 
# to modify the behavior of function or class.


# in simple word decorator is a 
# function that takes another function as an argument
# and extends the behavior of the latter function without explicitly modifying it.


# higher order function 
# is a function that takes another function as an argument
# or returns a function as a result.


# let simplify step by step :

# step 1
#---------------------------
# def outer_func():
#     print('hy outer function ')
#     def inner_fuc():
#         print('hy inner function')
#     print('by outer functio ')
# outer_func()
# inner_fuc()  # here is not call able outside the outer function
# #-------------------------------

# def outer_func():
#     print('hy outer function ')
#     def inner_fuc():
#         print('hy inner function')
#     print('by outer functio ')
#     inner_fuc()
# # outer_func()
# # it not show anything 

# #-----------------------------------

# def outer_func():
#     print('hy outer function ')
#     def inner_fuc():
#         print('hy inner function')
#     print('by outer functio ')
#     inner_fuc()
# outer_func()
# here it show first outer fuction body then inner

# #-------------------------------------------

# def outer_func():
#     print('hy outer function ')
#     def inner_fuc():
#         print('hy inner function')
#     print('by outer functio ')
#     return inner_fuc
# outer_func()

# # in this senario return statement send the reference of inner function
# # but not call


#-------------------------------------------

# def outer_func():
#     print('hy outer function ')
#     def inner_fuc():
#         print('hy inner function')
#     print('by outer functio ')
#     return inner_fuc()
# outer_func()

# in this senario return statement send the reference of inner function
# with call 
# but fiirst outer then inere 


#-------------------------------------------

def outer_func():
    print('hy outer function ')
    def inner_fuc():
        print('hy inner function')
    print('by outer functio ')
    return inner_fuc
result =outer_func()
print(result)

# in this senario return statement send the reference of inner function
# with  call 
# but fiirst outer then inere 