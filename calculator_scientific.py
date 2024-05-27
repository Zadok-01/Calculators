'Scientific Calculator'


from tkinter import *
import math


class SciCalc():
	def __init__(self):
		self.total = 0
		self.current = ''
		self.input_value = True
		self.check_sum = False
		self.op = ''
		self.result = False
	
	def clear_entry(self):
		self.result = False
		self.current = '0'
		self.display(0)
		self.input_value = True
	
	def clear_all(self):
		self.clear_entry()
		self.total = 0
	
	def number_enter(self, num):
		self.result = False
		num1 = txtDisplay.get()
		num2 = str(num)
		if self.input_value:
			self.current = num2
			self.input_value = False
		else:
			if num2 == '.':
				if num2 in num1:
					return
			self.current = num1 + num2
		self.display(self.current)
	
	def display(self, value):
		txtDisplay.delete(0, END)
		txtDisplay.insert(0, value)
	
	def equals(self):
		self.result = True
		self.current = float(self.current)
		if self.check_sum == True:
			self.valid_function()
		else:
			self.total = float(txtDisplay.get())
	
	def square_rt(self):
		self.result = False
		self.current = math.sqrt(float(txtDisplay.get()))
		self.display(self.current)
	
	def sgn(self):
		'Change sign'
		self.result = False
		self.current = -float(txtDisplay.get())
		self.display(self.current)
	
	def operation(self, op):
		'Handles operations + - x / mod sgn'
		self.current = float(self.current)
		if self.check_sum:
			self.valid_function()
		elif not self.result:
			self.total = self.current
			self.input_value = True
		self.check_sum = True
		self.op = op
		self.result = False
	
	def valid_function(self):
		'Details of operations + - x / mod sgn'
		if self.op == 'add':
			self.total += self.current
		elif self.op == 'sub':
			self.total -= self.current
		elif self.op == 'mult':
			self.total *= self.current
		elif self.op == 'div':
			self.total /= self.current
		elif self.op == 'mod':
			self.total %= self.current
		self.input_value = True
		self.check_sum = False
		self.display(self.total)
	
	def pi(self):
		self.result = False
		self.current = math.pi
		self.display(self.current)
	
	def cos(self):
		self.result = False
		self.current = math.cos(math.radians(float(txtDisplay.get())))
		self.display(self.current)
	
	def tan(self):
		self.result = False
		self.current = math.tan(math.radians(float(txtDisplay.get())))
		self.display(self.current)
	
	def sin(self):
		self.result = False
		self.current = math.sin(math.radians(float(txtDisplay.get())))
		self.display(self.current)
	
	def rad(self):
		self.result = False
		self.current = math.radians(float(txtDisplay.get()))
		self.display(self.current)
	
	def acos(self):
		self.result = False
		self.current = math.degrees(math.acos(float(txtDisplay.get())))
		self.display(self.current)
	
	def atan(self):
		self.result = False
		self.current = math.degrees(math.atan(float(txtDisplay.get())))
		self.display(self.current)
	
	def asin(self):
		self.result = False
		self.current = math.degrees(math.asin(float(txtDisplay.get())))
		self.display(self.current)
	
	def log(self):
		self.result = False
		self.current = math.log(float(txtDisplay.get()))
		self.display(self.current)
	
	def exp(self):
		self.result = False
		self.current = math.exp(float(txtDisplay.get()))
		self.display(self.current)
	
	def e(self):
		self.result = False
		self.current = math.e
		self.display(self.current)
	
	def log2(self):
		self.result = False
		self.current = math.log2(float(txtDisplay.get()))
		self.display(self.current)
	
	def deg(self):
		self.result = False
		self.current = math.degrees(float(txtDisplay.get()))
		self.display(self.current)
	
	def cosh(self):
		self.result = False
		self.current = math.cosh(math.radians(float(txtDisplay.get())))
		self.display(self.current)
	
	def sinh(self):
		self.result = False
		self.current = math.sinh(math.radians(float(txtDisplay.get())))
		self.display(self.current)
	
	def log10(self):
		self.result = False
		self.current = math.log10(float(txtDisplay.get()))
		self.display(self.current)
	
	def log1p(self):
		self.result = False
		self.current = math.log1p(float(txtDisplay.get()))
		self.display(self.current)
	
	def expml(self):
		self.result = False
		self.current = math.expm1(float(txtDisplay.get()))
		self.display(self.current)
	
	def lgamma(self):
		self.result = False
		self.current = math.lgamma(float(txtDisplay.get()))
		self.display(self.current)

sc = SciCalc()


def basic():
	root.resizable(width=False, height=False)
	root.geometry('465x535+0+0')


def scientific():
	root.resizable(width=False, height=False)
	root.geometry('930x535+0+0')


# GUI definition

root = Tk()
root.title('Scientific Calculator')
basic()

calc = Frame(root)
calc.grid()

txtDisplay = Entry(calc, font=('arial', 20, 'bold'), bg='bisque', 
					bd=15, width=29, justify=CENTER)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, '0')


# Number buttons

numberpad = '789456123'
i = 0
btn = []
for j in range(2, 5):
	for k in range(3):
		btn.append(Button(calc, width=6, height=2, 
						font=('arial', 20, 'bold'), bd=4, text=numberpad[i]))
		btn[i].grid(row=j, column=k, pady=1)
		btn[i]['command'] = lambda x=numberpad[i]: sc.number_enter(x)
		i += 1


# Basic Calculator Buttons

Button(calc, text='C', width=6, height=2, font=('arial', 20, 'bold'), 
		bd=4, bg='gray', command=sc.clear_entry
		).grid(row=1, column=0, pady=1)

Button(calc, text='CE', width=6, height=2, font=('arial', 20, 'bold'), 
		bd=4, bg='gray', command=sc.clear_all
		).grid(row=1, column=1, pady=1)

Button(calc, text='√', width=6, height=2, font=('arial', 20, 'bold'), 
		bd=4, bg='skyblue1', command=sc.square_rt
		).grid(row=1, column=2, pady=1)

Button(calc, text='+/-', width=6, height=2, font=('arial', 20, 'bold'), 
		bd=4, bg='skyblue1', command=sc.sgn
		).grid(row=1, column=3, pady=1)

Button(calc, text='x', width=6, height=2, font=('arial', 20, 'bold'), 
		bd=4, bg='skyblue1', command=lambda: sc.operation('mult')
		).grid(row=2, column=3, pady=1)

Button(calc, text='÷', width=6, height=2, font=('arial', 20, 'bold'), 
		bd=4, bg='skyblue1', command=lambda: sc.operation('div')
		).grid(row=3, column=3, pady=1)

Button(calc, text='-', width=6, height=2, font=('arial', 20, 'bold'), 
		bd=4, bg='skyblue1', command=lambda: sc.operation('sub')
		).grid(row=4, column=3, pady=1)

Button(calc, text='0', width=6, height=2, font=('arial', 20, 'bold'), 
		bd=4, command=lambda: sc.number_enter(0)
		).grid(row=5, column=0, pady=1)

Button(calc, text='.', width=6, height=2, font=('arial', 20, 'bold'), 
		bd=4, command=lambda: sc.number_enter('.')
		).grid(row=5, column=1, pady=1)

Button(calc, text='=', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='green', command=sc.equals
		).grid(row=5, column=2, pady=1)

btnAdd = Button(calc, text='+', width=6, height=2, font=('arial', 20, 'bold'), 
		bd=4, bg='skyblue1', command=lambda: sc.operation('add')
		).grid(row=5, column=3, pady=1)


# Scientific Calculator Buttons

Button(calc, text='𝝿', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.pi
		).grid(row=1, column=4, pady=1)

Button(calc, text='cos', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.cos
		).grid(row=1, column=5, pady=1)

Button(calc, text='tan', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.tan
		).grid(row=1, column=6, pady=1)

Button(calc, text='sin', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.sin
		).grid(row=1, column=7, pady=1)

Button(calc, text='rad', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.rad
		).grid(row=2, column=4, pady=1)

Button(calc, text='acos', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.acos
		).grid(row=2, column=5, pady=1)

Button(calc, text='atan', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.atan
		).grid(row=2, column=6, pady=1)

Button(calc, text='asin', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.asin
		).grid(row=2, column=7, pady=1)

Button(calc, text='log', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.log
		).grid(row=3, column=4, pady=1)

Button(calc, text='exp', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.exp
		).grid(row=3, column=5, pady=1)

Button(calc, text='mod', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
		bg='gold', command=lambda: sc.operation('mod')
		).grid(row=3, column=6, pady=1)

Button(calc, text='e', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.e
		).grid(row=3, column=7, pady=1)

Button(calc, text='log2', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.log2
		).grid(row=4, column=4, pady=1)

Button(calc, text='deg', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.deg
		).grid(row=4, column=5, pady=1)

Button(calc, text='cosh', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.cosh
		).grid(row=4, column=6, pady=1)

Button(calc, text='sinh', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.sinh
		).grid(row=4, column=7, pady=1)

Button(calc, text='log10', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.log10
		).grid(row=5, column=4, pady=1)

Button(calc, text='log1p', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.log1p
		).grid(row=5, column=5, pady=1)

Button(calc, text='expm1', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.expml
		).grid(row=5, column=6, pady=1)

Button(calc, text='lgamma', width=6, height=2, font=('arial', 20, 'bold'),
		bd=4, bg='gold', command=sc.lgamma
		).grid(row=5, column=7, pady=1)


# Menu

menubar = Menu(calc)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Mode', menu=filemenu)
filemenu.add_command(label='Basic', command=basic)
filemenu.add_command(label='Scientific', command=scientific)
root.config(menu=menubar)


root.mainloop()

