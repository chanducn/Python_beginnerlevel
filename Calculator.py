from tkinter import *
import parse
from math import factorial
import ast


# Window for calculator
root = Tk()
root.title("Chandu's Calculator" ) #Title of calculator



#adding the input field
display = Entry(root, font=("Arial", 18))
display.grid(row=0, column=0, columnspan=6, sticky=N+E+W+S, padx=5, pady=5)

# Configure grid weights for resizing
for i in range(6):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

# Code to add buttons
Button(root,text = '1',command = lambda:get_variables(1)).grid(row=2,column=0,sticky = N+E+W+S)
Button(root,text = '2',command = lambda:get_variables(2)).grid(row=2,column=1,sticky = N+E+W+S)
Button(root,text = '3',command = lambda:get_variables(3)).grid(row=2,column=2,sticky = N+E+W+S)
Button(root,text = '4',command = lambda:get_variables(4)).grid(row=3,column=0,sticky = N+E+W+S)
Button(root,text = '5',command = lambda:get_variables(5)).grid(row=3,column=1,sticky = N+E+W+S)
Button(root,text = '6',command = lambda:get_variables(6)).grid(row=3,column=2,sticky = N+E+W+S)
Button(root,text = '7',command = lambda:get_variables(7)).grid(row=4,column=0,sticky = N+E+W+S)
Button(root,text = '8',command = lambda:get_variables(8)).grid(row=4,column=1,sticky = N+E+W+S)
Button(root,text = '9',command = lambda:get_variables(9)).grid(row=4,column=2,sticky = N+E+W+S)

#Adding other buttons to calculator
Button(root,text ='AC',command=lambda : clear_all()).grid(row=5,column=0,sticky=N+S+E+W)
Button(root,text ='0',command=lambda : get_variables(0)).grid(row=5,column=1,sticky=N+S+E+W)
Button(root,text ='.',command=lambda : get_variables('.')).grid(row=5,column=2,sticky=N+S+E+W)

 
Button(root,text="+",command= lambda :get_operation("+")).grid(row=2,column=3, sticky=N+S+E+W)
Button(root,text="-",command= lambda :get_operation("-")).grid(row=3,column=3, sticky=N+S+E+W)
Button(root,text="*",command= lambda :get_operation("*")).grid(row=4,column=3, sticky=N+S+E+W)
Button(root,text="/",command= lambda :get_operation("/")).grid(row=5,column=3, sticky=N+S+E+W)
 
# adding new operations
Button(root,text="pi",command= lambda :get_operation("*3.14")).grid(row=2,column=4, sticky=N+S+E+W)
Button(root,text="%",command= lambda :get_operation("%")).grid(row=3,column=4, sticky=N+S+E+W)
Button(root,text="(",command= lambda :get_operation("(")).grid(row=4,column=4, sticky=N+S+E+W)
Button(root,text="exp",command= lambda :get_operation("**")).grid(row=5,column=4, sticky=N+S+E+W)
 
Button(root,text="<-",command= lambda :undo()).grid(row=2,column=5, sticky=N+S+E+W)
Button(root,text="x!", command= lambda: fact()).grid(row=3,column=5, sticky=N+S+E+W)
Button(root,text=")",command= lambda :get_operation(")")).grid(row=4,column=5, sticky=N+S+E+W)
Button(root,text="^2",command= lambda :get_operation("**2")).grid(row=5,column=5, sticky=N+S+E+W)
Button(root,text="=",command= lambda :calculate()).grid(columnspan=6, sticky=N+S+E+W)



i = 0    # Position o finsertion of digit

def get_variables(num): # num is the digit passed
    display.insert(END, num)


def get_operation(operator): # operator passed  + ,-
    global i 
    length =len(operator)
    display.insert(i,operator)
    i+=length


def clear_all():
    display.delete(0,END)

def undo():
    entire_string = display.get()  # Get the entire string
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()                   # clears the all string 
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")

def calculate():
    entire_string= display.get()
    try :
        a = compile(ast.parse(entire_string, mode='eval'), '<string>', 'eval')
        result = eval(a)    # evaluate 
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

root.mainloop() # starts the window