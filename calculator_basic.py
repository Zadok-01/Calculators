'Basic Calculator'
# Needs work to get button alignment correct


from tkinter import *
from tkinter import messagebox


calc = Tk()
calc.geometry('320x400')
calc.resizable(0, 0)  # Not resizable
calc.title('Calculator')


def about():
	messagebox.showinfo('About', 'Basic Calculator by Zadok')


def click_button(item):
	'Updates input field when button clicked'
	global expression
	inputText.set(inputText.get() + (str(item)))


def clear_button():
	'Clears latest input'
	global expression
	expression = ''
	inputText.set(inputText.get()[:-1])


def clear_all():
	inputText.set('')


def equal_button():
	'Evaluates expression'
	result = ''
	try:
		result = eval(inputText.get())
		inputText.set(result)
	except:
		result = '_ERROR_'
		inputText.set(result)


# MENU
menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Cut', accelerator='Ctrl + X')
filemenu.add_command(label='Copy', accelerator='Ctrl + C')
filemenu.add_command(label='Paste', accelerator='Ctrl + V')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=calc.quit)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='About', command=about)

menubar.add_cascade(label='Edit', menu=filemenu)
menubar.add_cascade(label='Help', menu=helpmenu)
calc.config(menu=menubar)  


# FRAME
expression = ''
inputText = StringVar()

inputFrame = Frame(calc, highlightbackground='grey')
inputFrame.pack(side=TOP)
inputField = Entry(inputFrame, font=('arial', 20), textvariable=inputText, 
				bg='black', fg='white', justify=RIGHT)
inputField.grid(row=0, column=0)
inputField.pack(ipady=10)

button_frame = Frame(calc)
button_frame.pack()


# BUTTONS

# Row 1
clearall = Button(button_frame, text='C', font=('arial', 20), fg='white', bg='black', 
				width=4, cursor='hand2', command=lambda: clear_all()
				).grid(row=1, column=0)
l_bracket= Button(button_frame, text = '(', font=('arial', 20), fg='white', bg='black', 
				width=4, cursor='hand2', command=lambda: click_button('(')
				).grid(row=1, column=1)
r_bracket = Button(button_frame, text=')', font=('arial', 20), fg='white', bg='black', 
				width=4, cursor='hand2', command=lambda: click_button(')')
				).grid(row=1, column=2)
clear = Button(button_frame, text='<', font=('arial', 20), fg='white', bg='black', 
				width=4, cursor='hand2', command=lambda: clear_button()
				).grid(row=1, column=3)

# Row 2
power = Button(button_frame, text = '^', font=('arial', 20), fg='white', bg='black', 
			width=4, cursor='hand2', command = lambda: click_button('**')
			).grid(row=2, column=0)
pie = Button(button_frame, text='π', font=('arial', 20), fg='white', bg='black', 
			width=4, cursor='hand2', command=lambda: click_button(3.1415926)
			).grid(row=2, column=1)
exp  = Button(button_frame, text='e', font=('arial', 20), fg='white', bg='black', 
			width=4, cursor='hand2', command = lambda: click_button(2.7182818)
			).grid(row=2, column=2)
divide_= Button(button_frame, text='/', font=('arial',20), fg='white', bg='black', 
			width=4, cursor='hand2', command = lambda: click_button('/')
			).grid(row=2, column=3)

# Row 3
seven = Button(button_frame, text='7', font=('arial', 20), fg='white', bg='black', 
			width=4, cursor='hand2', command=lambda: click_button(7)
			).grid(row=3, column=0)
eight = Button(button_frame, text='8', font=('arial', 20), fg='white', bg='black', 
			width=4, cursor='hand2', command=lambda: click_button(8)
			).grid(row=3, column=1)
nine = Button(button_frame, text='9', font=('arial', 20), fg='white', bg='black', 
			width=4, cursor='hand2', command=lambda: click_button(9)
			).grid(row=3, column=2)
multiply = Button(button_frame, text='*', font=('arial', 20), fg='white', bg='black', 
			width=4, cursor='hand2', command=lambda: click_button('*')
			).grid(row=3, column=3)

#Row 4
four = Button(button_frame, text='4', font=('arial', 20), fg='white', bg='black', 
			width=4, cursor='hand2', command=lambda: click_button(4)
			).grid(row=4, column=0)
five = Button(button_frame, text='5', font=('arial', 20), fg='white', bg='black', 
			width=4, cursor='hand2', command=lambda: click_button(5)
			).grid(row=4, column=1)
six = Button(button_frame, text='6', font=('arial', 20), fg='white', bg='black', 
			width=4, cursor='hand2', command=lambda: click_button(6)
			).grid(row=4, column=2)
minus = Button(button_frame, text='-', font=('arial', 20), fg='white', bg='black', 
			width=4, cursor ='hand2', command=lambda: click_button('-')
			).grid(row=4, column=3)

# Row 5
one = Button(button_frame, text='1', font=('arial', 20), fg='white', bg='black', 
			width=4, cursor='hand2', command=lambda: click_button(1)
			).grid(row=5, column=0)
two = Button(button_frame, text='2', font=('arial', 20), fg='white', bg='black', 
			width=4, cursor='hand2', command=lambda: click_button(2)
			).grid(row=5, column=1)
three = Button(button_frame, text='3', font=('arial', 20), fg='white', bg='black', 
			width=4, cursor='hand2', command=lambda: click_button(3)
			).grid(row=5, column=2)
plus = Button(button_frame, text='+', font=('arial', 20), fg='white', bg='black', 
			width=4, cursor='hand2', command=lambda: click_button('+')
			).grid(row=5, column=3)

# Row 6
point = Button(button_frame, text='.', font=('arial', 20), fg='white', bg='black', 
			width=4, cursor='hand2', command=lambda: click_button('.')
			).grid(row=6, column=0)
zero = Button(button_frame, text='0', font=('arial', 20), fg='white', bg='black', 
			width=4, cursor='hand2', command=lambda: click_button(0)
			).grid(row=6, column=1)
equals = Button(button_frame, text='=', font=('arial', 20), fg='red', bg='black', 
			width=8, cursor='hand2', command=lambda: equal_button()
			).grid(row=6, column=2, columnspan=2)


calc.mainloop()

