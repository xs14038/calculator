from tkinter import *

global label_text
label_text = ''
not_breaking_equals = False
root = Tk()
root.configure(bg = 'firebrick',)


def click():
    text = Label(text="hello there")
    text.pack()

def one():
    
    global label_text
    delete_list = list(label_text)
    if len(delete_list) <= 50:
        label_text = str(label_text + "1")
        output = Label(root, text=str(label_text))
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
    
def two():
    
    global label_text
    delete_list = list(label_text)
    if len(delete_list) <= 50:
        label_text = str(label_text + "2")
        output = Label(root, text=str(label_text))
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def three():
    
    global label_text
    delete_list = list(label_text)
    if len(delete_list) <= 50:
        label_text = str(label_text + "3")
        output = Label(root, text=str(label_text))
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def four():
    
    global label_text
    delete_list = list(label_text)
    if len(delete_list) <= 50:
        label_text = str(label_text + "4")
        output = Label(root, text=str(label_text))
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def five():
    
    global label_text
    delete_list = list(label_text)
    if len(delete_list) <= 50:
        label_text = str(label_text + "5")
        output = Label(root, text=str(label_text))
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def six():
    
    global label_text
    delete_list = list(label_text)
    if len(delete_list) <= 50:
        label_text = str(label_text + "6")
        output = Label(root, text=str(label_text))
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def seven():
    
    global label_text
    delete_list = list(label_text)
    if len(delete_list) <= 50:
        label_text = str(label_text + "7")
        output = Label(root, text=str(label_text))
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def eight():
    
    global label_text
    delete_list = list(label_text)
    if len(delete_list) <= 50:
        label_text = str(label_text + "8")
        output = Label(root, text=str(label_text))
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def nine():
    
    global label_text
    delete_list = list(label_text)
    if len(delete_list) <= 50:
        label_text = str(label_text + "9")
        output = Label(root, text=str(label_text))
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def zero():
    
    global label_text
    delete_list = list(label_text)
    if len(delete_list) <= 50:
        label_text = str(label_text + "0")
        output = Label(root, text=str(label_text))
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def decimal():
    
    global label_text
    delete_list = list(label_text)
    if len(delete_list) <= 49:
        label_text = str(label_text + ".")
        output = Label(root, text=str(label_text))
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def multiply():
    
    global label_text
    delete_list = list(label_text)
    if len(delete_list) <= 49:
        if delete_list[-1] != '5':
            label_text = str(label_text + "*")
            output = Label(root, text=str(label_text))
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def divide():
    
    global label_text
    delete_list = list(label_text)
    if len(delete_list) <= 49:
        label_text = str(label_text + "/")
        output = Label(root, text=str(label_text))
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def plus():
    
    global label_text
    delete_list = list(label_text)
    if len(delete_list) <= 49:
        label_text = str(label_text + "+")
        output = Label(root, text=str(label_text))
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def subtract():
    
    global label_text
    delete_list = list(label_text)
    if len(delete_list) <= 49:
        label_text = str(label_text + "-")
        output = Label(root, text=str(label_text))
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def AC():
    
    global label_text
    label_text = str("")
    output = Label(root, text=str(label_text))
    output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def equals():
    
    global label_text
    label_text= str(eval(label_text))
    output = Label(root, text=str(label_text))
    output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
    
def delete():
    
    global label_text

    delete_list = list(label_text)
    del delete_list[-1]
    delete_list = ''.join(delete_list)
    label_text = delete_list
    output = Label(root, text=str(label_text))
    output.grid(row=0, column=0, columnspan=5, sticky=NSEW)



buttons=Frame(root)
buttons.grid(columnspan=5, rowspan=5, ipady=200, ipadx=200)

output = Label(root, text=str(label_text))
one = Button(root, text="1", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=one)
two = Button(root, text="2", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=two)
three = Button(root, text="3", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=three)
four = Button(root, text="4", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=four)
five = Button(root, text="5", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=five)
six = Button(root, text="6", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=six)
seven = Button(root, text="7", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=seven)
eight = Button(root, text="8", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=eight)
nine = Button(root, text="9", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=nine)
zero = Button(root, text="0", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=zero)
multiply = Button(root, text="*", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=multiply)
divide = Button(root, text="/", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=divide)
plus = Button(root, text="+", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=plus)
subtract = Button(root, text="-", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=subtract)
equals = Button(root, text="=", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=equals)
AC = Button(root, text="AC", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=AC)
decimal = Button(root, text=".", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=decimal)
delete = Button(root, text="Del", font=("Comic Sans MS", "15"), bg = "cornsilk", fg = "goldenrod", command=delete)




output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
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
equals.grid(row=3, column=4, rowspan=2, sticky=NSEW)
AC.grid(row=1, column=4, sticky=NSEW)
decimal.grid(row=4, column=2, sticky=NSEW)
delete.grid(row=2, column=4, sticky=NSEW)



     
root.title("Charles")



        

        

root.mainloop()       
        
