from time import *
import random

def mistake(paratest,usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[0]!=usertest[0]:
                error = error + 1

        except:
            error = error + 1

    return error                
def speed_time(s_time,e_time,userprint):
    time_delay = e_time - s_time
    time_r = round(time_delay,2)
    speed = (len(userprint)/time_r)
    return round(speed)



sentence = ["my name is naveen","your name is khelawan","her name is nidhi"]
word = random.choice(sentence)
print("****welcom to typing test****")
print(word)
print()

time_1 = time()
userinput = input("enter the sentense ")
time_2 = time()

print('speed :',speed_time(time_1,time_2,userinput))
print('error :',mistake(word,userinput))