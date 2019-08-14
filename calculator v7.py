from tkinter import *

label_text = ''
not_breaking_equals = False
not_breaking_equals_2 = False
root = Tk()
label_equals = ''


def one():
    
    global label_text
    global not_breaking_equals_2
    global label_equals
    delete_list = list(label_text)
    if not_breaking_equals_2 == True:
        label_text = ''
        label_equals = ''
        label_text = str(label_text + "1")
        label_equals = str(label_equals + "1")
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        not_breaking_equals_2 = False
    elif not_breaking_equals == False:
        if len(delete_list) <= 17:
            label_text = str(label_text + "1")
            label_equals = str(label_equals + "1")
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def two():
    
    global label_text
    global not_breaking_equals_2
    global label_equals
    delete_list = list(label_text)
    if not_breaking_equals_2 == True:
        label_text = ''
        label_equals = ''
        label_text = str(label_text + "2")
        label_equals = str(label_equals + "2")
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        not_breaking_equals_2 = False
    elif not_breaking_equals == False:
        if len(delete_list) <= 17:
            label_text = str(label_text + "2")
            label_equals = str(label_equals + "2")
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def three():
    
    global label_text
    global not_breaking_equals_2
    global label_equals
    delete_list = list(label_text)
    if not_breaking_equals_2 == True:
        label_text = ''
        label_equals = ''
        label_text = str(label_text + "3")
        label_equals = str(label_equals + "3")
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        not_breaking_equals_2 = False
    elif not_breaking_equals == False:
        if len(delete_list) <= 17:
            label_text = str(label_text + "3")
            label_equals = str(label_equals + "3")
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def four():
    
    global label_text
    global not_breaking_equals_2
    global label_equals
    delete_list = list(label_text)
    if not_breaking_equals_2 == True:
        label_text = ''
        label_equals = ''
        label_text = str(label_text + "4")
        label_equals = str(label_equals + "4")
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        not_breaking_equals_2 = False
    elif not_breaking_equals == False:
        if len(delete_list) <= 17:
            label_text = str(label_text + "4")
            label_equals = str(label_equals + "4")
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def five():
    
    global label_text
    global not_breaking_equals_2
    global label_equals
    delete_list = list(label_text)
    if not_breaking_equals_2 == True:
        label_text = ''
        label_equals = ''
        label_text = str(label_text + "5")
        label_equals = str(label_equals + "5")
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        not_breaking_equals_2 = False
    elif not_breaking_equals == False:
        if len(delete_list) <= 17:
            label_text = str(label_text + "5")
            label_equals = str(label_equals + "5")
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def six():
    
    global label_text
    global not_breaking_equals_2
    global label_equals
    delete_list = list(label_text)
    if not_breaking_equals_2 == True:
        label_text = ''
        label_equals = ''
        label_text = str(label_text + "6")
        label_equals = str(label_equals + "6")
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        not_breaking_equals_2 = False
    elif not_breaking_equals == False:
        if len(delete_list) <= 17:
            label_text = str(label_text + "6")
            label_equals = str(label_equals + "6")
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def seven():
    
    global label_text
    global not_breaking_equals_2
    global label_equals
    delete_list = list(label_text)
    if not_breaking_equals_2 == True:
        label_text = ''
        label_equals = ''
        label_text = str(label_text + "7")
        label_equals = str(label_equals + "7")
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        not_breaking_equals_2 = False
    elif not_breaking_equals == False:
        if len(delete_list) <= 17:
            label_text = str(label_text + "7")
            label_equals = str(label_equals + "7")
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def eight():
    
    global label_text
    global not_breaking_equals_2
    global label_equals
    delete_list = list(label_text)
    if not_breaking_equals_2 == True:
        label_text = ''
        label_equals = ''
        label_text = str(label_text + "8")
        label_equals = str(label_equals + "8")
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        not_breaking_equals_2 = False
    elif not_breaking_equals == False:
        if len(delete_list) <= 17:
            label_text = str(label_text + "8")
            label_equals = str(label_equals + "8")
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def nine():
    
    global label_text
    global not_breaking_equals_2
    global label_equals
    delete_list = list(label_text)
    if not_breaking_equals_2 == True:
        label_text = ''
        label_equals = ''
        label_text = str(label_text + "9")
        label_equals = str(label_equals + "9")
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        not_breaking_equals_2 = False
    elif not_breaking_equals == False:
        if len(delete_list) <= 17:
            label_text = str(label_text + "9")
            label_equals = str(label_equals + "9")
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def zero():
    
    global label_text
    global not_breaking_equals_2
    global label_equals
    delete_list = list(label_text)
    if not_breaking_equals_2 == True:
        label_text = ''
        label_equals = ''
        label_text = str(label_text + "0")
        label_equals = str(label_equals + "0")
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        not_breaking_equals_2 = False
    elif not_breaking_equals == False:
        if len(delete_list) <= 17:
            label_text = str(label_text + "0")
            label_equals = str(label_equals + "0")
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def decimal():
    
    global label_text
    global not_breaking_equals_2
    global label_equals
    jump = 0
    delete_list = label_text.replace('/','!')
    delete_list = delete_list.replace('*','!')
    delete_list = delete_list.replace('-','!')
    delete_list = delete_list.replace('+','!')
    delete_list = delete_list.split('!')
    decimal_check = delete_list[len(delete_list)-1]
    if not_breaking_equals_2 == True:
        label_text = ''
        label_equals = ''
        label_text = str(label_text + ".")
        label_equals = str(label_equals + ".")
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        not_breaking_equals_2 = False
    if delete_list[len(delete_list)-1] == '':
        label_text = str(label_text + ".")
        label_equals = str(label_equals + ".")
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
    for x in decimal_check:
        if x == '.':
            error = True
        else:
            if '.' in delete_list[len(delete_list)-1]:
                error = True
            if '.' not in delete_list[len(delete_list)-1]:
                if not_breaking_equals == False:
                    if len(label_text) <= 17:
                        if len(label_text) == 0:
                            jump = 1
                        elif '.' != label_text[-1]:
                            jump = 1
    if jump == 1:
        label_text = str(label_text + ".")
        label_equals = str(label_equals + ".")
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)

def multiply():
    
    global label_text
    global not_breaking_equals
    global not_breaking_equals_2
    global label_equals
    delete_list = label_equals.split(' ')
    if delete_list[-1] == '0':
        label_text = ''.join(delete_list)
    elif delete_list[-1] != '':
        delete_list[-1] = delete_list[-1].lstrip('0')
        if delete_list[-1] == '':
            delete_list[-1] = '0'
        label_text = ''.join(delete_list)
        label_equals = label_text
    delete_list = list(label_text)
    if not_breaking_equals_2 == True:
        error = True
    elif len(delete_list) <= 17 and len(delete_list) != 0:
        if delete_list[-1] != '*' and delete_list[-1] != '/' and delete_list[-1] != '+' and delete_list[-1] != '-' and delete_list[-1] != '.':
            label_equals = str(label_text + '* ')
            label_text = str(label_text + "*")
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
    not_breaking_equals = False

def divide():
    
    global label_text
    global not_breaking_equals
    global not_breaking_equals_2
    global label_equals
    delete_list = label_equals.split(' ')
    if delete_list[-1] == '0':
        label_text = ''.join(delete_list)
    elif delete_list[-1] != '':
        delete_list[-1] = delete_list[-1].lstrip('0')
        if delete_list[-1] == '':
            delete_list[-1] = '0'
        label_text = ''.join(delete_list)
        label_equals = label_text
    delete_list = list(label_text)
    if not_breaking_equals_2 == True:
        error = True
    elif len(delete_list) <= 17 and len(delete_list) != 0:
        if delete_list[-1] != '*' and delete_list[-1] != '/' and delete_list[-1] != '+' and delete_list[-1] != '-' and delete_list[-1] != '.':
            label_equals = str(label_text + '/ ')
            label_text = str(label_text + "/")
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
    not_breaking_equals = False

def plus():
    
    global label_text
    global not_breaking_equals
    global not_breaking_equals_2
    global label_equals
    delete_list = label_equals.split(' ')
    if delete_list[-1] == '0':
        label_text = ''.join(delete_list)
    elif delete_list[-1] != '':
        delete_list[-1] = delete_list[-1].lstrip('0')
        if delete_list[-1] == '':
            delete_list[-1] = '0'
        label_text = ''.join(delete_list)
        label_equals = label_text
    delete_list = list(label_text)
    if not_breaking_equals_2 == True:
        label_text = ''
        label_equals = ''
        label_equals = str(label_text + '+ ')
        label_text = str(label_text + "+")
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        not_breaking_equals_2 = False
    elif len(delete_list) <= 17:
        if len(delete_list) == 0:
            label_equals = str(label_text + '+ ')
            label_text = str(label_text + "+")
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        elif delete_list[-1] != '*' and delete_list[-1] != '/' and delete_list[-1] != '+' and delete_list[-1] != '.' and delete_list[-1] != '-':
            label_equals = str(label_text + '+ ')
            label_text = str(label_text + "+")
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
    not_breaking_equals = False

def subtract():
    
    global label_text
    global not_breaking_equals
    global not_breaking_equals_2
    global label_equals
    delete_list = label_equals.split(' ')
    if delete_list[-1] == '0':
        label_text = ''.join(delete_list)
    elif delete_list[-1] != '':
        delete_list[-1] = delete_list[-1].lstrip('0')
        if delete_list[-1] == '':
            delete_list[-1] = '0'
        label_text = ''.join(delete_list)
        label_equals = label_text
    delete_list = list(label_text)
    if not_breaking_equals_2 == True:
        label_text = ''
        label_equals = ''
        label_equals = str(label_text + '- ')
        label_text = str(label_text + "-")
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        not_breaking_equals_2 = False
    elif len(delete_list) <= 17:
        if len(delete_list) == 0:
            label_equals = str(label_text + '- ')
            label_text = str(label_text + "-")
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        elif delete_list[-1] != '/' and delete_list[-1] != '.':
            label_equals = str(label_text + '- ')
            label_text = str(label_text + "-")
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
    not_breaking_equals = False

def AC():
    
    global label_text
    global not_breaking_equals
    global not_breaking_equals_2
    global label_equals
    label_text = str("")
    label_equals = str('')
    output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
    output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
    not_breaking_equals = False

def equals():
    
    global label_text
    global not_breaking_equals
    global not_breaking_equals_2
    global label_equals
    delete_list = label_equals.split(' ')
    if delete_list[-1] == '' and delete_list[0] != delete_list[-1]:
        label_text = ''.join(delete_list)
        delete_list = ''.join(delete_list)
        output = Label(root, text="Missing number after operator", font=("Helvetica", "20"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        not_breaking_equals_2 = True
    elif delete_list[-1] == '0':
        label_text = ''.join(delete_list)
        delete_list = ''.join(delete_list)
    else:
        delete_list[-1] = delete_list[-1].lstrip('0')
        if delete_list[-1] == '' and delete_list[0] != '':
            delete_list[-1] = '0'
        label_text = ''.join(delete_list)
        delete_list = ''.join(delete_list)
        label_equals = label_text

    if label_text == '':
        error = True
    elif delete_list[-1] == '-' or delete_list[-1] == '+' or delete_list[-1] == '*' or delete_list[-1] == '/' or delete_list[-1] == '.':
        error = True
    else:
        try:
            label_text = str(eval(label_text))
            label_equals = str(eval(label_text))
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
            not_breaking_equals = True
        except ZeroDivisionError:
            output = Label(root, text="Can't divide by zero", font=("Helvetica", "20"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
            not_breaking_equals_2 = True

def delete():
    
    global label_text
    global not_breaking_equals
    global label_equals
    label_equals = list(label_equals)
    if ''.join(label_equals) == '':
        error = True
    elif str(label_equals[-1]) == ' ':
        del label_equals[-2]
        del label_equals[-1]
    elif len(label_equals) != 0:
        del label_equals[-1]
    label_equals = ''.join(label_equals)
    label_text = label_equals
    if str(label_text) == '':
        not_breaking_equals = False
    if not_breaking_equals_2 == False:
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
    not_breaking_equals = False

buttons=Frame(root)
buttons.grid(columnspan=5, rowspan=5, ipady=200, ipadx=210)

output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
one = Button(root, text="1", font=("Helvetica", "30"), bg="Gray20", fg="Gray85", command=one)
two = Button(root, text="2", font=("Helvetica", "30"), bg="Gray20", fg="Gray85", command=two)
three = Button(root, text="3", font=("Helvetica", "30"), bg="Gray20", fg="Gray85", command=three)
four = Button(root, text="4", font=("Helvetica", "30"), bg="Gray20", fg="Gray85", command=four)
five = Button(root, text="5", font=("Helvetica", "30"), bg="Gray20", fg="Gray85", command=five)
six = Button(root, text="6", font=("Helvetica", "30"),bg="Gray20", fg="Gray85", command=six)
seven = Button(root, text="7", font=("Helvetica", "30"), bg="Gray20", fg="Gray85", command=seven)
eight = Button(root, text="8", font=("Helvetica", "30"), bg="Gray20", fg="Gray85", command=eight)
nine = Button(root, text="9", font=("Helvetica", "30"), bg="Gray20", fg="Gray85", command=nine)
zero = Button(root, text="0", font=("Helvetica", "30"), bg="Gray20", fg="Gray85", command=zero)
multiply = Button(root, text="*", font=("Helvetica", "30"), bg="Gray80", fg="Gray20", command=multiply)
divide = Button(root, text="/", font=("Helvetica", "30"), bg="Gray80", fg="Gray20", command=divide)
plus = Button(root, text="+", font=("Helvetica", "30"), bg="Gray80", fg="Gray20", command=plus)
subtract = Button(root, text="-", font=("Helvetica", "30"), bg="Gray80", fg="Gray20", command=subtract)
equals = Button(root, text="=", font=("Helvetica", "30"), bg="Gray80", fg="Gray20", command=equals)
AC = Button(root, text="AC", font=("Helvetica", "30"), bg="Gray80", fg="Gray20", command=AC)
decimal = Button(root, text=".", font=("Helvetica", "30"), bg="Gray20", fg="Gray85", command=decimal)
delete = Button(root, text="Del", font=("Helvetica", "30"), bg="Gray80", fg="Gray20", command=delete)

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
root.resizable(0,0)
root.mainloop()

