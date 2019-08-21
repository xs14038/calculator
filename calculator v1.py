from tkinter import *


root = Tk()
root.configure(bg = 'firebrick',)


def click():
    text = Label(text="hello there")
    text.pack()


buttons=Frame(root)
buttons.grid(columnspan=5, rowspan=5, ipady=200, ipadx=200)

one = Button(root, text="1", command=click)
two = Button(root, text="2", command=click)
three = Button(root, text="3", command=click)
four = Button(root, text="4", command=click)
five = Button(root, text="5", command=click)
six = Button(root, text="6", command=click)
seven = Button(root, text="7", command=click)
eight = Button(root, text="8", command=click)
nine = Button(root, text="9", command=click)
zero = Button(root, text="0", command=click)
multiply = Button(root, text="x", command=click)
divide = Button(root, text="/", command=click)
plus = Button(root, text="+", command=click)
subtract = Button(root, text="-", command=click)
equals = Button(root, text="=", command=click)
AC = Button(root, text="AC", command=click)
decimal = Button(root, text=".", command=click)
delete = Button(root, text="Del", command=click)





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
        
