from tkinter import*
import tkinter as tk
import string
import random

def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_box.get())

    pasword=random.sample(all,password_length)
    passwordFiled.insert(0,pasword)  

def reset():
    passwordFiled.delete(0, tk.END)

root=Tk()
root.config(bg='brown')
Font=('arial',13,'bold')

passwordLabel=Label(root,text='Password Generator',font=('times new roman',20,'bold'),fg='white',bg='brown')
passwordLabel.grid(pady=5)

lengthLabel=Label(root,text='Password Length',font=Font,fg='white',bg='brown')
lengthLabel.grid(pady=5)

length_box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_box.grid(pady=5)

generateButton=Button(root,text="Generate",font=Font,bg="white",fg='black',command=generator)
generateButton.grid(pady=5)

resetButton=Button(root,text="Reset",font=Font,fg='black',bg='white',command=reset)
resetButton.grid(pady=5)

passwordFiled=Entry(root,width=35,bd=2,font=Font)
passwordFiled.grid(pady=5)

root.mainloop()
  