# name1 = input("enter your name")
# height1 = int(input("enter height"))
# weight1 = int(input("enter your weight"))


# def bmi_calculator(name,height_m,weight):
#     BMI = height1/(weight1**2)

# a = bmi_calculator(name1,height1,weight1)
# print(a)


# def calci(x,z):
#     print(x**2,z)   

# calci(4,8)

# def mivalue():
#     return 1,2,3
# a,b,c = mivalue()
# print('a =',a)
# print('b =',b)
# print('c =',c)
# 
# def greet(firstname,lastname):
#     print(f"my name is {firstname} {lastname}")

# greet("naveen","chandrawanshi")

# def name(a,b,c,d):
#     print(a,b,c,d)

# name("naveen","khelawan","dk","bhargavi")


# def function(*args):
#     for item in args:
#         print(item)
    
# har = ["naveen","khelawan","dk","mansi","nidhi"]
# function(*har)
import random

word_list = ["naveen","khelawan","kajal"]
chosen_word = random.choice(word_list)
guess = input("enter the name: ").lower()
for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")

        