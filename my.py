from tkinter import *
from tkinter.messagebox import showinfo

def is_palindrome(word):
    return word == word[::-1]

def check_palindrome():
    word = (entry.get()) 
    is_palindrome(word)
    if is_palindrome(word):
        result_label.config(text=f"{word} is a palindrome")
    else:
        result_label.config(text=f"{word} is not a palindrome")
    
root = Tk()
root.geometry("250x150")
root.title("Palindromic")

label = Label(root, text="Check If it is a Palindrome or not")
label.pack(fill=BOTH, expand=1)

entry = Entry(root)
entry.pack(fill=BOTH, expand=1)

result_label = Label(root, text="")
result_label.pack(fill=BOTH, expand=1)

button = Button(root, text="Check", command=check_palindrome)
button.pack(fill=BOTH, expand=1)

root.mainloop()
