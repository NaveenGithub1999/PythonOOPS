# naveen = ["23","34","25"]
# print(naveen[0])
# print(naveen[2])

# naveen = {'march7':23,'march8':25,}
# print(naveen['march7'])
# def get_squerd_number(number):
#     squre_number = []
#     for n in number:
#         squre_number.append(n*n)
#     return squre_number 
# number  = [2,3,4,5]
# get_squerd_number(number)

# numbers = [3,4,2,5,6,3,1,4]
# for i in range(len(numbers)):
#     for j in range(i+1,len(numbers)):
#         if numbers[i] == numbers[j]:
#             print(str(numbers[i]) + " is a dupliacte")
#             break

# import random

# def guess(x):
#     random_number = random.randint(1,x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'enter the value between 1 and x: {x}'))
#         if guess > random_number:
#             print('over valued')
            
#         else:
#             print("cprrect value")  
#             break  
# guess(10)
# numbers = 0
# for i in range((numbers(1,))):
#     if numbers[i] == 68:
#         print("you have the no {i}")
#     else:
#         print("wrong no.{i}")    

# email recognizer//////////////////////////////////////////////



# email = input("enter your email !")
# s,j,d=0,0,0
# if len(email)>=6:
#     if email[0].isalpha():
#         if (email[-4]==".") ^ (email[-3]=="."):
#             for i in email:
#                 if i==i.isspace():
#                     s=1
            
#                 elif i==i.isupper():
#                     d==1
                
#                 elif i==i.isdigit():
#                     continue
#                 else:
#                     j=1           
#             if j==1 or s==1 or d==1 :
#                 print('wrong email nav')
#         else:
#              print("wrong email 3")
#     else:
#         print("wrong email 2")            

# else:
#     print("wrong email 1")    
##############################################
x = int(input("enter the value "))
i = 0
for i in range(i, x):
    if i==x:
        break
    else:
        i = i+1
        print(i)
