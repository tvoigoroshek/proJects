import random
from tkinter import *
tk = Tk()
tk.title("КНБ")
lbl = Label(tk, text="Выберите один из предложенных вариантов:", font=("",16))
lbl.grid(column=0, row=0)
lbl1change = Label(tk, text="", font=("",12))
lbl1change.grid(column=0, row=1)
i=0
##while (i==0):
##    player=0

def rock():
    player=1
    bot=random.randint(1,3)
    if bot==1:
        print("Компьютер выбрал камень")         
        lbl1change.config(text=("Ничья"))
    if bot==2:
        print("Компьютер выбрал ножницы")      
        lbl1change.config(text=("Выигрыш"))
    if bot==3:
        print("Компьютер выбрал бумага")   
        lbl1change.config(text=("Проигрыш"))

def scissors():
    player=2
    bot=random.randint(1,3)
    if bot==1:
        print("Компьютер выбрал камень")         
        lbl1change.config(text=("Проигрыш"))
    if bot==2:
        print("Компьютер выбрал ножницы")      
        lbl1change.config(text=("Ничья"))
    if bot==3:
        print("Компьютер выбрал бумага")
        lbl1change.config(text=("Выигрыш"))

def paper():
    player=3
    bot=random.randint(1,3)
    if bot==1:
        print("Компьютер выбрал камень")         
        lbl1change.config(text=("Выигрыш"))
    if bot==2:
        print("Компьютер выбрал ножницы")      
        lbl1change.config(text=("Проигрыш"))
    if bot==3:
        print("Компьютер выбрал бумага")
        lbl1change.config(text=("Ничья"))
        
btn1 = Button(tk, text="Камень",command=rock, font=("",12))
btn1.grid(column=0, row=2)
btn2 = Button(tk, text="Ножницы",command=scissors, font=("",12))
btn2.grid(column=0, row=3)
btn3 = Button(tk, text="Бумага",command=paper, font=("",12))
btn3.grid(column=0, row=4)
    
            


tk.mainloop
