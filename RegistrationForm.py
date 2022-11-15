
from cProfile import label
from tkinter import *


root = Tk()
root.geometry("500x300")
root.title("Registration Form")
Label(root, text="Registration for games",).grid(row =0,column=3)
def Getvalue():
    print("Accepted")

name = Label(root, text="name")
Phone = Label(root, text="Phone")
gender = Label(root, text="gender")
city = Label(root, text="city")



name.grid(row =1,column=1)
Phone.grid(row =2,column=1)
gender.grid(row =3,column=1)
city.grid(row =4,column=1)

namevalue = StringVar
Phonevalue = IntVar
gendervalue = StringVar
cityvalue = StringVar
checkvalue  = IntVar


nameentry = Entry(root, textvariable = "namevalue")

Phoneentry = Entry(root, textvariable = "Phonevalue")

genderentry = Entry(root, textvariable = "gendervalue")

cityentry = Entry(root, textvariable = "cityvalue")



nameentry.grid(row =1,column=3)
Phoneentry.grid(row =2,column=3)
genderentry.grid(row =3,column=3)
cityentry.grid(row =4,column=3)

Button(text = "submit",command="Getvalue",).grid(row=6, column=3)


root.mainloop()