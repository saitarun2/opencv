from image import openph
from tkinter import *
root1 = Tk()
root1.title("Photo Searcher")
root1.geometry("500x200")
root1.resizable(0, 0)
def func1():
    root2 = Tk()
    root2.geometry("500x300")
    root2.resizable(0, 0)
    root2.title("Pictures")
    var = StringVar(root2)
    label = Label(root2, text="welcome", font=("Arial", 25), fg="violet").grid(row=0, column=1, columnspan=2)
    label1 = Label(root2, text="Enter Name :", font=("panton rust", 15), fg="dark blue").grid(row=1, column=0, pady=20,sticky=W)
    entry = Entry(root2, textvariable=var, font=("Arial", 15)).grid(row=1, column=1, columnspan=2)
    button1 = Button(root2, text="Show ", font=("Arial", 25), fg="dark green", command = lambda : openph(var)).grid(row=2, column=1,columnspan=2)
    root2.mainloop()
    root3 = Tk()
    root3.geometry("200x200")
    root3.resizable(0,0)
    root3.title('The End')
    label2 = Label(root3, text = 'Thank you', font = ('pantom rust',20)).pack()
label = Label(root1, text="Gallery", font=("Arial", 15), fg="white", bg="red").pack()
button1 = Button(root1, text="Open Image", font=("Arial", 20), fg="skyblue", command=func1).pack(pady=40)
root1.mainloop()