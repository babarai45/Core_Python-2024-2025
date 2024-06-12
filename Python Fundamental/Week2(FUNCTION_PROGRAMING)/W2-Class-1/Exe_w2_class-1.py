`# --------------------------
# what is list comprehension ?
# list comprehension is concise of element to creating
# new list using in single line  and apply function of each new  element
# syntax :
# newline_name=[ expression/output, loop, condition/optionals ]

# ----------- Example:- 01 simple
# result = [i*2 for i in range(5)]
# print(result)
#
# # ----------- Example:- 02 with Expression
# result = [(i+2)**2 for i in range(1, 10,)]
# print(result)
#
#
# # ----------- Example:- 03 Expression+condition
# result = [(i+2)**2 for i in range(1, 10,) if i % 2 == 0]
# print(result)


# # ----------- Example:- 04
# result = [i for i in range(10, 100, 5) if i > 20]
# print(result)

#
# # ----------- Example:- 05 Expression+double if conditions
# result = [(i + 2) ** 2 for i in range(1, 10, ) if i > 2 if i % 2 == 0]
# print(result)


# ----------- Example:- 06 Expression+if else conditions
# result = ['True' if i % 2 == 0 else 'wrong' 'corrector i == 3 else 'totally wrongdoer i in range(1, 10, ) if i > 4]
# print(result)


# # ----------- Example:- 05 Expression+double + nested loop
# result = [(a+i) for i in range(5) for a in range(7) if (a+i)%2==0]
# print(result)


# # ----------- Example:- 05 Expression+double + nested loop
# lst = [1, 2, 3, 4]
# lst2 = ['a', 'b', 'c', 'd']
# result = [(y,x) for x in lst for y in lst2]
# print(result)


# ---------------------------------- CHALLENGES
# ----- Question 01:-
# 1. Write a function that takes a list of integers as input and returns a new list containing
# only the positive integers, using a list comprehension and a conditional statement.

# # --sol 1 by for loop scratch

# user_input = input("Enter list of integer by space").split()
# list_of = []
# positive_int = []
# for i in user_input:
#     list_of.append(int(i))
# for y in list_of:
#     if y > 0:
#         positive_int.append(y)
# print(positive_int)


# # --- using list comprehension

# list_of_integer = list(map(int, input('Enter list of integer by space ').split()))
# positive = [i for i in list_of_integer if i > 0]
# print(positive)

# ------- using function


# def positive_integer(x):
#     list_of = []
#     positive_integer_num = []
#     for i in x:
#         list_of.append(int(i))
#     for j in list_of:
#         if j > 0:
#             positive_integer_num.append(j)
#     return positive_integer_num


# try:
#     user_input = input("Enter list of integer by space").split()
#     result = positive_integer(user_input)
#     print(result)

# except ValueError as e:
#     print("invalid input", e)
# finally:
#     print("program executed ")


# ----- Question 02:-
# 3. Create a function that takes a list of strings as input and returns a new
# list with all the strings that are palindromes, using a while loop and a ternary operator.
 
# SOLUTION 01
user_inputs =input("Enter list of strings !").split()
palindron = []
i=0
while i< len(user_inputs):
    valu = user_inputs[i]
    if valu == valu[::-1]:
        palindron.append(valu)
    else:
        print('not',valu)
    i+=1
print(user_inputs)
print(type(user_inputs))
for i in user_inputs:
    print(type(i))

str2='level'
print(str2[0::])
print(str2[::-1])
