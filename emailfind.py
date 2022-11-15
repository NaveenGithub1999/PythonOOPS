email = input("enter your email !")
s,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if (email[-4]==".") ^ (email[-3]=="."):
            for i in email:
                if i==i.isspace():
                    s=1
            
                elif i==i.isupper():
                    d==1
                
                elif i==i.isdigit():
                    continue
                else:
                    j=1           
            if j==1 or s==1 or d==1 :
               print('wrong email ')
        else:
            print("wrong email 3")
    else:
        print("wrong email 2")            

else:
    print("wrong email 1")    





# desc = input("enter the description !")

# for i in len(desc):
#     if i==i.isdigit():
#         i=i+1
# print(i)    
# 
# ###############################    
# content = input("enter the desc")
# a=range(0,len(content))
# for line in content:
     
#     for i in line:
         
#         # Checking for the digit in
#         # the string
#         if i.isdigit() == True:
             
#             a= int(i)
 
# print("The sum is:", a[])    

#####################################################################
# importing the module
# import re

# # string
# desc = input("sprx reactivate account has ! ")

# # extracting the mobile number
# Phonenumber=re.compile(r'\d\d\d\d\d\d')
# m=Phonenumber.search(desc)
# RX = m.group()
# # printing the result 
# print(f'mobile number found from the string : {RX}')
# if len(RX)>6 or len(RX)<6:
#     print("wrong rx no")

# else:
#     print(f'rx {RX}')