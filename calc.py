from tkinter import *
app = Tk()
app.geometry("400x500")
app.title("sadique software pvt ltd")
data = StringVar()
exq = ""
data.set("0")
def press(n):
    global exq
    global data  
    exq += n
    data.set(exq)
def total():
    global exq
    data.set(eval(exq))
def clearBtn():
    global exq
    data.set("0")
    exq = ""
display = Entry(app,width=22,font=("Arial",22),textvariable=data)
display.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
one = Button(app,text="1",font=("Arial",22),width=4, height=2, command=lambda: press("1"))
one.grid(row=1,column=0,padx=5,pady=5)
two = Button(app,text="2",font=("Arial",22),width=4, height=2,  command=lambda: press("2"))
two.grid(row=1,column=1,padx=5,pady=5)
three = Button(app,text="3",font=("Arial",22),width=4, height=2,  command=lambda: press("3"))
three.grid(row=1,column=2,padx=5,pady=5)
four = Button(app,text="+",font=("Arial",22),width=4, height=2,  command=lambda: press("+"))
four.grid(row=1,column=3,padx=5,pady=5)
five = Button(app,text="4",font=("Arial",22),width=4, height=2,  command=lambda: press("4"))
five.grid(row=2,column=0,padx=5,pady=5)
btn6 = Button(app,text="5",font=("Arial",22),width=4, height=2,  command=lambda: press("5"))
btn6.grid(row=2,column=1,padx=5,pady=5)
btn7 = Button(app,text="6",font=("Arial",22),width=4, height=2,  command=lambda: press("6"))
btn7.grid(row=2,column=2,padx=5,pady=5)
btn8 = Button(app,text="-",font=("Arial",22),width=4, height=2,  command=lambda: press("-"))
btn8.grid(row=2,column=3,padx=5,pady=5)
btn9 = Button(app,text="7",font=("Arial",22),width=4, height=2,  command=lambda: press("7"))
btn9.grid(row=3,column=0,padx=5,pady=5)
btn10 = Button(app,text="8",font=("Arial",22),width=4, height=2,  command=lambda: press("8"))
btn10.grid(row=3,column=1,padx=5,pady=5)
btn11 = Button(app,text="9",font=("Arial",22),width=4, height=2,  command=lambda: press("9"))
btn11.grid(row=3,column=2,padx=5,pady=5)
btn12 = Button(app,text="/",font=("Arial",22),width=4, height=2,  command=lambda: press("/"))
btn12.grid(row=3,column=3,padx=5,pady=5)
btn13 = Button(app,text="0",font=("Arial",22),width=4, height=2,  command=lambda: press("0"))
btn13.grid(row=4,column=0,padx=5,pady=5)
btn14 = Button(app,text="C",font=("Arial",22),width=4, height=2,bg="red",fg="white",command=clearBtn)
btn14.grid(row=4,column=1,padx=5,pady=5)
btn15 = Button(app,text="=",font=("Arial",22),width=4, height=2,command=total)
btn15.grid(row=4,column=2,padx=5,pady=5)
btn16 = Button(app,text="*",font=("Arial",22),width=4, height=2,  command=lambda: press("*"))
btn16.grid(row=4,column=3,padx=5,pady=5)
app.mainloop()


