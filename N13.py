import tkinter as tk
from tkinter import messagebox
mainWindow=tk.Tk()
mainWindow.title("Calculator")
heading_label=tk.Label(mainWindow,text="Enter first number")
heading_label.pack()
n1_field=tk.Entry(mainWindow)
n1_field.pack()
heading_label=tk.Label(mainWindow,text="Enter the second number")
heading_label.pack()
n2_field=tk.Entry(mainWindow)
n2_field.pack()
heading_label=tk.Label(mainWindow,text="Operations")
heading_label.pack()
def addition():
    a=int(n1_field.get())
    b=int(n2_field.get())
    print(a+b)
def subs():
    a=int(n1_field.get())
    b=int(n2_field.get())
    if(a>b):
        print(a-b)
    else:
        print(b-a)
def mult():
    a=int(n1_field.get())
    b=int(n2_field.get())
    print(a*b)
def div():
    a=int(n1_field.get())
    b=int(n2_field.get())
    if(b is not 0):
        print(a/b)
    else:
        messagebox.showerror("Error","Cannot divide by 0.")
        print("Math Error")

button1=tk.Button(mainWindow,text="+",command=lambda:addition())
button1.pack()
button2=tk.Button(mainWindow,text="-",command=lambda:subs())
button2.pack()
button3=tk.Button(mainWindow,text="*",command=lambda:mult())
button3.pack()
button4=tk.Button(mainWindow,text="/",command=lambda:div())
button4.pack()
mainWindow.mainloop()


