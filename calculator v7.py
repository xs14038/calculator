from tkinter import *
# allows the use of the UI

# importing global variables
label_text = ''
not_breaking_equals = False
not_breaking_equals_2 = False
root = Tk()
label_equals = ''


# defining what happens when you press the one button
def one():

    # importing global variables
    global label_text
    global not_breaking_equals_2
    global label_equals
    # list used for an if statement
    delete_list = list(label_text)
    # in case an error message is on the screen
    if not_breaking_equals_2 == True:
        # redefining variables used for the display
        label_text = ''
        label_equals = ''
        label_text = str(label_text + "1")
        label_equals = str(label_equals + "1")
        # outputting the display so the user can see the number they inputed
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        # allowing the use of buttons that couldn't be used when the error message was up
        not_breaking_equals_2 = False
        # If equals was the last button pressed the user cannot enter numbers as there is a number present
    elif not_breaking_equals == False:
        # so it doesn't expand the application
        if len(delete_list) <= 17:
            # redefining variables used for the display
            label_text = str(label_text + "1")
            label_equals = str(label_equals + "1")
            # outputting the display so the user can see the number they inputed
            output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
            output.grid(row=0, column=0, columnspan=5, sticky=NSEW)


# defining the two button, all numbers have the same code apart from the number so look at 1 to see what it does
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
    # jump is used if the code meets the requirements given to save some lines of coding
    jump = 0
    # making all the functions ! for easy list making
    delete_list = label_text.replace('/','!')
    delete_list = delete_list.replace('*','!')
    delete_list = delete_list.replace('-','!')
    delete_list = delete_list.replace('+','!')
    delete_list = delete_list.split('!')
    decimal_check = delete_list[len(delete_list)-1]
    # same as with the numbers
    if not_breaking_equals_2 == True:
        label_text = ''
        label_equals = ''
        label_text = str(label_text + ".")
        label_equals = str(label_equals + ".")
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        not_breaking_equals_2 = False
    # if the last number after the function is blank a decimal point may be placed
    if delete_list[len(delete_list)-1] == '':
        label_text = str(label_text + ".")
        label_equals = str(label_equals + ".")
        output = Label(root, text=str(label_text), font=("Helvetica", "30"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
    # checking if there is already a decimal point in that number
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
                        # making sure the previous input isn't .
                        elif '.' != label_text[-1]:
                            jump = 1
    # goes to this if requirements are met
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
    # splits the variable for easy manipulation
    delete_list = label_equals.split(' ')
    if delete_list[-1] == '0':
        label_text = ''.join(delete_list)
    # used to solve numbers with leading 0s
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
    # allows numbers to be placed afterwards if equals has been pressed
    not_breaking_equals = False


def plus():

    # you can start the input with a plus as my stakeholder and I decided it would be best so an error wouldn't pop up
    # if someone was to do so. You can't place a plus after a multiplication or divide as we decided that it looks a bit
    # weird and didn't want to confuse those using it.
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
        # symbols add a space after the symbol in the label_equals as we can then split it into a list without changing
        # any part of the code
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
        # so you can't place one after a symbol
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
    # an error message if someone ends with an operator
    if delete_list[-1] == '' and delete_list[0] != delete_list[-1]:
        label_text = ''.join(delete_list)
        delete_list = ''.join(delete_list)
        output = Label(root, text="Missing number after operator", font=("Helvetica", "20"), bg="Gray20", fg="Gray85")
        output.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        not_breaking_equals_2 = True
    # getting rid of leading zeros
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

    # so you don't get an error by typing nothing
    if label_text == '':
        error = True
    elif delete_list[-1] == '-' or delete_list[-1] == '+' or delete_list[-1] == '*' or delete_list[-1] == '/' or delete_list[-1] == '.':
        error = True
    else:
        # try and except block incase they divide by zero
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
    # so it deletes the symbol from label equals as well as label text
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

# making buttons for grid layout
buttons=Frame(root)
buttons.grid(columnspan=5, rowspan=5, ipady=200, ipadx=210)

# organising what the buttons look like on the UI and what happens when they click them
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

# sorting out where the buttons appear in the window
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

# Charles starts with a C so my stakeholder and I decided it would be a fitting calculator name to add personality
root.title("Charles")
# so you can't expand the window as all the buttons are a set size
root.resizable(0,0)
# runs the window
root.mainloop()

