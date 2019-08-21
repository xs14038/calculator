from tkinter import *


root = Tk()
root.configure(bg = 'firebrick',)


def click():
    text = Label(text="hello there")
    text.pack()


buttons=Frame(root)
buttons.grid(columnspan=5, rowspan=5, ipady=200, ipadx=200)

one = Button(root, text="1", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod")
two = Button(root, text="2", font=("Comic Sans MS", "15"))
three = Button(root, text="3", font=("Comic Sans MS", "15"))
four = Button(root, text="4", font=("Comic Sans MS", "15"))
five = Button(root, text="5", font=("Comic Sans MS", "15"))
six = Button(root, text="6", font=("Comic Sans MS", "15"))
seven = Button(root, text="7", font=("Comic Sans MS", "15"))
eight = Button(root, text="8", font=("Comic Sans MS", "15"))
nine = Button(root, text="9", font=("Comic Sans MS", "15"))
zero = Button(root, text="0", font=("Comic Sans MS", "15"))
multiply = Button(root, text="x", font=("Comic Sans MS", "15"))
divide = Button(root, text="/", font=("Comic Sans MS", "15"))
plus = Button(root, text="+", font=("Comic Sans MS", "15"))
subtract = Button(root, text="-", font=("Comic Sans MS", "15"))
equals = Button(root, text="=", font=("Comic Sans MS", "15"))
AC = Button(root, text="AC", font=("Comic Sans MS", "15"))
decimal = Button(root, text=".", font=("Comic Sans MS", "15"))
delete = Button(root, text="Del", font=("Comic Sans MS", "15"))





one.grid(row=3, column=0, sticky=NSEW)
two.grid(row=3, column=1, sticky=NSEW)
three.grid(row=3, column=2, sticky=NSEW)
four.grid(row=2, column=0, sticky=NSEW)
five.grid(row=2, column=1, sticky=NSEW)
six.grid(row=2, column=2, sticky=NSEW)
seven.grid(row=1, column=0, sticky=NSEW)
eight.grid(row=1, column=1, sticky=NSEW)
nine.grid(row=1, column=2, sticky=NSEW)
zero.grid(row=4, column=0, columnspan=2, sticky=NSEW)
multiply.grid(row=3, column=3, sticky=NSEW)
divide.grid(row=4, column=3, sticky=NSEW)
plus.grid(row=1, column=3, sticky=NSEW)
subtract.grid(row=2, column=3, sticky=NSEW)
equals.grid(row=3, column=4, sticky=NSEW)
AC.grid(row=1, column=4, sticky=NSEW)
decimal.grid(row=4, column=2, sticky=NSEW)
delete.grid(row=2, column=4, sticky=NSEW)



     
root.title("calculator")



        

        

root.mainloop()       
        
