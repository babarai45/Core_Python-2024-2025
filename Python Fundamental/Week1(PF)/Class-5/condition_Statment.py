# problem: space found and not found using while or break
# First Method
# lang = "python programing fundamental"
# i = 0
# while i < len(lang):
#     if lang[i] == " ":
#         print("Space Found")
#         break
#     i += 1
# else:
#     print("Not Found")

#   ----------------------------------------------------
# Second Method
# lang = "python programing fundamental"
# flag = True
# i = 0
# while i < len(lang):
#     if lang[i] == " ":
#         flag = False
#         print("Space Found")
#         break
#     i += 1
# if flag:
#     print("Not Found")


#   second Problem :
user_name = ['babar','alice','bob','carol','david','eve']
while True:
    new_user = input("enter name ")
    if new_user in user_name:
        print(new_user,"name is already taken")
    else:
        user_name.append(new_user)
        print("user name has been added",new_user)
    print(user_name)
    again = input("Do you want to play again?(y/n)")
    if again.lower() != "y":
        print("Thank you for playing")
        break


# using while loop
i=0
user_name = ['babar','alice','bob','carol','david','eve']
new_user = []
while i<len(user_name):
    if user_name[i] in user_name:
        new_user.append(user_name[i])
        i+=1
        print(new_user)
        user_name = new_user