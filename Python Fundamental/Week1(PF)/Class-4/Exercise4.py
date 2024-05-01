# -----------Question:-2

# 2. Implement a program that prompts the user to enter a list of integers and a target sum,
#  and then prints out all the pairs of numbers in the list that add up to the target sum, 
# using the membership operator `in`.


# ------------here is first to take lsit of integer :
# # #------------- Method-01-----using for loop 
# User_input=input("enter lsit of integer ").split()
# # target=int(input("enter target value "))
# list_of_interger=[]
# for i in User_input:
#     list_of_interger.append(int(i))

# print(list_of_interger)
# print(User_input)


# ---------------------------------------------
# Solution-01 by scrach using for loop
# ---------------------------------------------
# # Get the list of integers from the user
#
# User_input = input("Enter lsit of integer by sapce  ").split()
# lsit_of = []
# for i in User_input:
#     lsit_of.append(int(i))
# print(lsit_of)
# target = int(input("enter sum of target value "))
# pair = []
# for i in range(len(lsit_of)):
#     for j in range(i + 1, len(lsit_of)):
#         if target == lsit_of[i] + lsit_of[j]:
#             pair.append((lsit_of[i], lsit_of[j]))
# print(pair)

# -------------- Solution-02------using while loop

# User_input=input("Enter lsit of integer by sapce  ")
# split_input=User_input.split()
# list_of_interger=[]
# i=0
# while i< len(split_input):
#     list_of_interger.append(int(split_input[i]))
#     i+=1
# print(list_of_interger)
# target_Sum=int(input("Enter Target value :-"))
# x=0
# y=0+1
# pair=[]
# while x<len(list_of_interger):
#     x+=1
#     while y<len(list_of_interger):
#         if list_of_interger[x]+list_of_interger[y]==target_Sum:
#             pair.append((list_of_interger[x],list_of_interger[y]))
#         y+=1
# print(pair)

# ------------Method-03--------- using function 
# def find_pairs(nums, target):
#     pairs = []
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if target == nums[i] + nums[j]:
#                 pairs.append((nums[i], nums[j]))
#     return pairs
# def main():
#     try:
#         User_input = input("Enter a list of integers separated by spaces: ").split()
#         lsit_of = [int(num) for num in User_input]
#     except ValueError:
#         print("Please enter valid integers separated by spaces.")
#         return
#     print("Input list:", lsit_of)
#     try:
#         target = int(input("Enter the target sum: "))
#     except ValueError:
#         print("Please enter a valid integer for the target sum.")
#         return
#     pairs = find_pairs(lsit_of, target)
#     if pairs:
#         print("Pairs that add up to the target sum:", pairs)
#     else:
#         print("No pairs found that add up to the target sum.")
# if __name__ == "__main__":
#     main()

# _______________________________ without any Execution handling
# def find_pair(num, target):
#     pair = []
#     for i in range(len(num)):
#         for j in range(i + 1, len(num)):
#             if target == num[i] + num[j]:
#                 pair.append((num[i], num[j]))
#     return pair
#
#
# try:
#     user_input = input('Enter list of integer by space ').split()
#     list_integer = [int(i) for i in user_input]
#     target_value = int(input('Enter target value'))
#     result = find_pair(list_integer, target_value)
#     print(result)
# except ValueError as e:
#     print('Please enter valid integer value', e)
# else:
#     print('No pair found')
# finally:
#     print('Program is completed')

#-------------------------------lambda function
# user_input = list(map(int, input("Enter list of integer separated by space ").split()))
# target_value = int(input("Enter Target value "))
# pair = lambda x:[[(x[i],x[j]) for i in range(len(x)) for j in range(i+1,len(x)) if x[i] + x[j] == target_value]] 
# print(pair(user_input))


# --------------------using list comprehension :
# user_input = list(map(int,input("Enter list of integer separated Space  ").split()))
# target_value = int(input("Enter Target Value "))
# pair = [(user_input[i],user_input[j]) for i in range(len(user_input)) for j in range(i+1,len(user_input)) if user_input[i] + user_input[j] == target_value]
# print(pair)

# # -------------------- using map function
# user_input = list(map(int, input("Enter list of integer separated by space ").split()))
# target_value = int(input("Enter Target Value ")) 
# pair = list(map(lambda x: [(x[i], x[j]) for i in range(len(x)) for j in range(i + 1, len(x)) if x[i] + x[j] == target_value], [user_input]))
# print(pair)

# ----------------------- using filter function
# user_input = list(map(int, input("Enter list of integer separated by space ").split()))
# target_value = int(input("Enter Target Value "))
# pair = list(filter(lambda x: x[0] + x[1] == target_value, [(user_input[i], user_input[j]) for i in range(len(user_input)) for j in range(i + 1, len(user_input))]))
# print(pair)

# # ----------------------- using reduce function
# from functools import reduce
# user_input = list(map(int, input("Enter list of integer separated by space ").split()))
# target_value = int(input("Enter Target Value "))
# pair = reduce(lambda x, y: x + y, [[(user_input[i], user_input[j]) for i in range(len(user_input)) for j in range(i + 1, len(user_input)) if user_input[i] + user_input[j] == target_value]])
# print(pair)

# -------  using recursion
# def find_pair(num, target):
#     if not num:
#         return []
#     return [(num[0], x) for x in num[1:] if num[0] + x == target] + find_pair(num[1:], target)


# try:
#     user_input = input('Enter list of integer by space ').split()
#     list_integer = [int(i) for i in user_input]
#     target_value = int(input('Enter target value'))
#     result = find_pair(list_integer, target_value)
#     print(result)
# except ValueError as e:
#     print('Please enter valid integer value', e)
# else:
#     print('No pair found')
# finally:
#     print('Program is completed')


# ----------------------- Questions:-4

# 4. Write a program that takes a string as input and prints out the string
# with all the vowels replaced by their bitwise complement, using bitwise
# operators.
# def complement_vowels(input_string):
#     vowels = 'aeiouAEIOU'
#     result = ''
#     for char in input_string:
#         if char in vowels:
#             # Bitwise complement operation: XOR with 0b1111111 (binary representation of 127)
#             complement_char = chr(ord(char) ^ 0b11111111)
#             result += complement_char
#         else:
#             result += char
#     return result
#
#
# input_string = input("Enter a string: ")
# print("Original string:", input_string)
# print("String with vowels replaced by their bitwise complement:", complement_vowels(input_string))



# ----------------------- Questions:-5

# 5. Implement a function that takes a list of integers and returns
# a new list with all the elements that are
# not divisible by 3 or 5, using the ternary operator.

def filter_numbers(numbers):
    return [num for num in numbers if (num % 3 != 0) and (num % 5 != 0)]

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
filtered_numbers = filter_numbers(numbers)
print("Original list:", numbers)
print("Filtered list (not divisible by 3 or 5):", filtered_numbers)
 