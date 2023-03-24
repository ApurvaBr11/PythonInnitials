from tkinter import *
import time

root = Tk()
root.title("tik")

def display_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(200, display_time)

clock_label = Label(root, font=('calibri', 28, 'bold'), bg='#2D2727', fg='#AEC2B6')
clock_label.pack(fill=BOTH, expand=1)

display_time()
root.mainloop()
