# recursive function:
# calll itself function like loop

#  squre root implementation 


# def func(base,exp):
#     if exp == 0:
#         return 1
#     return base * func(base,exp-1)
# result=func(5,3)
# print(result)


# using for loop

# # 5x5x5 =125     (5^3)
# def sqr(base,exp):
#     result =1
#     for _ in range(exp):
#          result = base * result
#     return result
# root=sqr(5,3)
# print(root)


# two list 
l1=[1,2,3,4]
l2=['babar','ali','hamza','mohsin']

dic={}
for i in range(len(l1)):
    dic[l1[i]]=[l2[i]]
print(dic)