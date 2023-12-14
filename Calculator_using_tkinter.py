import math as m
from tkinter import *
import tkinter.font as tkFont
from tkinter import font



root= Tk()

root.title("Fitness Calculator")


root.configure(bg='black')

e= Entry(root,text="Enter Value", width=80)

e.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

menu_bar = Menu(root)

menu_1 = Menu(menu_bar, tearoff=0)
menu_2 = Menu(menu_bar, tearoff=0)
menu_3 = Menu(menu_bar, tearoff=0)

menu_1.add_command(label="Standard")
menu_1.add_command(label="Scientific")
menu_1.add_separator()
menu_1.add_command(label="Date Calculation")
menu_1.add_command(label="Graph")
menu_2.add_command(label="BMI")
menu_2.add_command(label="Volume")
menu_2.add_separator()
menu_2.add_command(label="Length")
menu_2.add_command(label="Temperature")
menu_3.add_command(label="Exit", command=root.destroy)



menu_bar.add_cascade(label="Calculator", menu=menu_1)
menu_bar.add_cascade(label="Convertor", menu=menu_2)
menu_bar.add_cascade(label="Exit", menu=menu_3)




root.config(menu=menu_bar)








def weight():
    k=int(second_number)/((f_num/100)**2)
    print



def button_click(number):
   #e.delete(0, END)
    current= e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))

    
def button_clear():
    e.delete(0, END)
    
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
    if math == "power":
        e.insert(0, f_num ** int(second_number))
    if math == "percentage":
        e.insert(0, f_num*int(second_number)/100)

   
def button_Weight():
   second_number = e.get()
   e.delete(0,END)
   global math
   math= "weight"
   if math == "weight":
       e.insert(0, int(second_number)/((f_num/100)**2))
       




def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

   
def button_percentage():
    first_number = e.get()
    global f_num
    global math
    math = "percentage"
    f_num = int(first_number)
    e.delete(0, END)
    
    
    
def button_power():
    first_number = e.get()
    global f_num
    global math
    math = "power"
    f_num = int(first_number)
    e.delete(0, END)

def button_sin():
    first_number = e.get()
    global f_num
    global math
    math = "sin"
    f_num = int(first_number)
    if math == "sin":
        e.insert(0, m.sin(f_num))
    

    
  
    
def button_squareroot():
    first_number = e.get()
    global f_num
    global math
    math = "squareroot"
    f_num = int(first_number)
    if math == "squareroot":
        e.insert(0,m.sqrt(f_num))
    
    
def button_Height():
    first_number = e.get()
    global f_num
    global math
    math = "height"
    f_num = int(first_number)
    e.delete(0, END)
   
   
def button_log():
    first_number = e.get()
    global f_num
    global math
    math = "log"
    f_num = int(first_number)
    if math == "log":
        e.insert(0, m.log10(f_num))

def button_cos():
    first_number=e.get()
    global f_num
    global math
    math ="cos"
    f_num = int(first_number)
    if math == "cos":
        e.insert(0, m.cos(f_num))
    
    


    
button_1 = Button(root, text="  1  ", padx=40, pady=20,fg="white",activebackground="#00ff00", bg="Black", command=lambda: button_click(1))
button_2 = Button(root, text="  2  ", padx=40, pady=20,fg="White",activebackground="#00ff00", bg="Black", command=lambda: button_click(2))
button_3 = Button(root, text="        3        ", padx=40, pady=20,activebackground="#00ff00",fg="White", bg="Black", command=lambda: button_click(3))
button_4 = Button(root, text="  4  ", padx=40, pady=20,fg="White",activebackground="#00ff00", bg="Black", command=lambda: button_click(4))
button_5 = Button(root, text="  5  ", padx=40, pady=20,fg="White",activebackground="#00ff00", bg="Black", command=lambda: button_click(5))
button_6 = Button(root, text="        6       ", padx=40, pady=20,activebackground="#00ff00",fg="White", bg="Black", command=lambda: button_click(6))
button_7 = Button(root, text="  7  ", padx=40, pady=20,fg="White",activebackground="#00ff00", bg="Black", command=lambda: button_click(7))
button_8 = Button(root, text="  8  ", padx=40, pady=20,fg="White",activebackground="#00ff00", bg="Black", command=lambda: button_click(8))
button_9 = Button(root, text="        9        ", padx=40, pady=20,activebackground="#00ff00",fg="White", bg="Black", command=lambda: button_click(9))
button_0 = Button(root, text="  0  ", padx=40, pady=20, fg="White",activebackground="#00ff00", bg="Black",command=lambda: button_click(0))
button_add = Button(root, text="  +  ", padx=40, pady=20,fg="White",activebackground="#00ff00", bg="Black", command=button_add)
button_equal = Button(root, text="         =         ", padx=40, pady=20,activebackground="#00ff00",fg="White", bg="Black", command=button_equal)

button_clear = Button(root, text="Clear", padx=40, pady=20,fg="White", bg="Black",activebackground="#00ff00", command= button_clear)
button_power = Button(root, text="      x^y        ", padx=40, pady=20,fg="White", bg="Black",activebackground="#00ff00", command=button_power)
button_squareroot = Button(root, text="          √        ", padx=40, pady=20, fg="White", bg="Black",activebackground="#00ff00",command=button_squareroot)
button_percentage= Button(root, text ="          %        " , padx=40, pady=20,fg="White", bg="Black",activebackground="#00ff00", command=button_percentage)
button_subtract = Button(root, text="  -  ", padx=40, pady=20,fg="White", bg="Black",activebackground="#00ff00", command=button_subtract)
button_multiply = Button(root, text="  *  ", padx=40, pady=20,fg="White", bg="Black",activebackground="#00ff00", command=button_multiply)
button_divide = Button(root, text="  /  ", padx=40, pady=20,fg="White", bg="Black",activebackground="#00ff00", command=button_divide)
button_cos =Button(root, text= "      cos      ", padx=40, pady=20,fg="White", bg="Black",activebackground="#00ff00", command=button_cos)
button_Height =Button(root, text=" Height(cm)" ,padx= 40, pady=20,fg="White", bg="Black",activebackground="#00ff00", command=button_Height)
button_Weight =Button(root, text="Weight(Kg)" ,padx= 40, pady=20,fg="White", bg="Black",activebackground="#00ff00", command=button_Weight)
button_log= Button(root, text= "     log         ", padx= 40, pady=20,fg="White", bg="Black",activebackground="#00ff00", command=button_log)
button_sin= Button(root, text= "     sin         ", padx= 40, pady=20,fg="White", bg="Black",activebackground="#00ff00", command=button_sin)

  




button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)
button_clear.grid(row=7, column=0)
button_equal.grid(row=7, column=3)
button_add.grid(row=6, column=0)

button_subtract.grid(row=5,column=1)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=7,column=1)

button_power.grid(row=2,column=3)
button_squareroot.grid(row=3,column=3)
button_percentage.grid(row=4, column=3)
button_cos.grid(row=5, column=2)


button_Height.grid(row=5, column=3)
button_Weight.grid(row=6, column=3)
button_log.grid(row=6, column=2)
button_sin.grid(row=7, column=2)



root.mainloop()

