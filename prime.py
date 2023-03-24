from tkinter import *
from tkinter.messagebox import showinfo


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def check_prime():
    num = int(entry.get())
    if is_prime(num):
        showinfo("Result", f"{num} is a prime number!")
    else:
        showinfo("Result", f"{num} is not a prime number.")

root = Tk()
root.geometry("250x150")
root.title("Prime Number Checker")

label = Label(root, text="Enter a number:")
label.pack(fill=BOTH, expand=1)

entry = Entry(root)
entry.pack(fill=BOTH, expand=1)

button = Button(root, text="Check", command=check_prime)
button.pack(fill=BOTH, expand=1)

root.mainloop()
