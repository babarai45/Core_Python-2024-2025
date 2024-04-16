#class 3 codes proof and examples 
# 1.pint() function
# syntax: print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

print("welcome to python class 3")
print(2+5)
print("welcome to python class 3", 2+5)
print("welcome to python class 3", 2+5, sep='--')
print("welcome to python class 3", 2+5, sep='--', end=' ')
print("welcome to python class 3", 2+5, sep='--', end=' ', flush=False)  


# the default value of sep is ' ' and end is '\n'
# the default value of print() is None
# the default value of flush is False
a=print()
print(a) # None


# print() function for multiple values
print("Hello", "World", "Python") # Hello World Python
# print() function or output formatting .format() method
print("Hello {} World {} Python".format("Python", "World")) # Hello Python World World Python
print("Hello {1} World {0} Python".format("Python", "World")) # Hello World World Python
print("Hello {name} World {place} Python".format(name="Python", place="World")) # Hello Python World Python





# 2. input() function

#syntax: input(prompt)
#prompt: A string, representing a default message before the input.

#input() function always returns a string value

name = input("Enter your name: ")
print("Hello", name)
print(type(name))  # <class 'str'>

# input function has parameter prompt, which is optional 
# if we do not provide the prompt, then it will not display anything on the console
# input() function always returns a string value
# if we want to take integer input, then we have to typecast the input value to int 
# if we want to take float input, then we have to typecast the input value to float

age = int(input("Enter your age: "))
print("Your age is", age) # return type of age is int

age=float(input("Enter your age: "))
print("Your age is", age) # return type of age is float

age=bool(input("Enter your age: "))
if age.isnumeric():
    print("You entered True")
else:
    print("You entered False")

 
# 3. typecasting
# syntax: type(value)

# if we want to take integer input, then we have to typecast the input value to int
# if we want to take float input, then we have to typecast the input value to float
# if we want to take boolean input, then we have to typecast the input value to bool
# if we want to take list input, then we have to typecast the input value to list
# if we want to take tuple input, then we have to typecast the input value to tuple
# if we want to take set input, then we have to typecast the input value to set
# if we want to take dictionary input, then we have to typecast the input value to dictionary



# 4. eval() function 
    # eval(expression, globals=None, locals=None)
    # we can pass only 3 arguments in eval function 
    # eval function is used to evaluate the value of the string and return the result 
    # eval function always returns the value of the expression in the form of the data type of the expression
    # eval function is used to evaluate the expression, not the statement

# syntax: eval
#eval function take only one argument and that is string 
#eval function always returns the value of the expression in the form of the data type of the expression
#eval function is used to evaluate the expression, not the statement(we can not use print statement in eval function)
#eval function is used to evaluate the value of the string and return the result
    
a = eval("2+5") # it take the expression as string and return the value of the expression
print(a) # 7

b = eval("2.5+5.5") # it take the expression as string and return the value of the expression
print(b) # 8.0


# 5. exec() function
    # exec function is used to execute the statement and return the result 
    # exec function does not return anything 
    # exec function is used to execute the statement, not the expression

# syntax: exec
#exec function take only one argument and that is string
#exec function does not return anything
#exec function is used to execute the statement, not the expression(we can use print statement in exec function)
#exec function is used to execute the statement and return the result

exec("print('Hello World')") # Hello World
exec("a=2+5") # it take the statement as string and execute the statement
print(a) # 7


# 6. ord() function
    # ord function is used to get the ASCII value of the character
    # ord function always returns the ASCII value of the character


# syntax: ord
#ord function take only one argument and that is string
#ord function always returns the ASCII value of the character

print(ord('A')) # 65
print(ord('a')) # 97
print(ord('1')) # 49
print(ord(' ')) # 32
print(ord('@')) # 64
print(ord('!')) # 33
print(ord('z')) # 122


# 7. chr() function
    # chr function is used to get the character of the ASCII value
    # chr function always returns the character of the ASCII value

# syntax: chr
#chr function take only one argument and that is integer
#chr function always returns the character of the ASCII value

print(chr(65)) # A
print(chr(97)) # a
print(chr(49)) # 1
print(chr(32)) # (space)
print(chr(64)) # @


# 8. bin() function
    # bin function is used to get the binary value of the integer
    # bin function always returns the binary value of the integer

# syntax: bin
#bin function take only one argument and that is integer
#bin function always returns the binary value of the integer

print(bin(5)) # 0b101
print(bin(10)) # 0b1010
print(bin(15)) # 0b1111


# 9. oct() function
    # oct function is used to get the octal value of the integer
    # oct function always returns the octal value of the integer

# syntax: oct

#oct function take only one argument and that is integer
#oct function always returns the octal value of the integer

print(oct(5)) # 0o5
print(oct(10)) # 0o12
print(oct(15)) # 0o17


# 10. hex() function
    # hex function is used to get the hexadecimal value of the integer
    # hex function always returns the hexadecimal value of the integer

# syntax: hex
#hex function take only one argument and that is integer

print(hex(5)) # 0x5
print(hex(10)) # 0xa
print(hex(15)) # 0xf



# 11. abs() function
    # abs function is used to get the absolute value of the number
    # abs function always returns the positive value of the number

# syntax: abs
#abs function take only one argument and that is number

print(abs(-5)) # 5
print(abs(-10)) # 10


# 12. round() function
    # round function is used to get the round off value of the number
    # round function always returns the round off value of the number

# syntax: round
#round function take only one argument and that is number

print(round(5.5)) # 6
print(round(5.4)) # 5


# 13. pow() function
    # pow function is used to get the power of the number
    # pow function always returns the power of the number

# syntax: pow
#pow function take two argument and that is number and power

print(pow(2, 3)) # 8 # here 2 is the number and 3 is the power of the number
print(pow(3, 2)) # 9
print(pow(5, 3)) # 125