from tkinter import *

expression = "" 


def press(num): 

	global expression 

	expression = expression + str(num) # Nối số vừa bấm vào biểu thức

	equation.set(expression) # Cập nhật nội dung ô nhập



def equalpress(): 

	try: 

		global expression 

		total = str(eval(expression)) 

		equation.set(total) 
		expression = "" 


	except: 

		equation.set(" error ") 
		expression = "" 

def clear(): 
	global expression 
	expression = "" 
	equation.set("") 

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)


# Driver code 
if __name__ == "__main__": 
	gui = Tk() 

	
	gui.configure(background="light green") 

	
	gui.title("Simple Calculator") 

	
	gui.geometry("350x200") 

	 
	equation = StringVar() 

	
	expression_field = Entry(gui, textvariable=equation) 

	
	expression_field.grid(columnspan=4, ipadx=120)

	# Dòng 2
	cls = Button(gui, text='Cls', fg='black', bg='white',
					command=clear, height=1, width=7)
	cls.grid(row=2, column=0, padx=0, pady=0, sticky="ew")


	black = Button(gui, text='Black', fg='black', bg='white',
					command=backspace, height=1, width=7)
	black.grid(row=2, column=1, padx=0, pady=0, sticky="ew")


	drum = Button(gui, text='', fg='black', bg='white',
					command=None, height=1, width=7)
	drum.grid(row=2, column=2, padx=0, pady=0, sticky="ew")


	close = Button(gui, text='Close', fg='black', bg='white',
					command=gui.quit, height=1, width=7)
	close.grid(row=2, column=3, padx=0, pady=0, sticky="ew")

	
	# Dòng 3
	button7 = Button(gui, text='7', fg='black', bg='white',
					command=lambda: press(7), height=1, width=7)
	button7.grid(row=3, column=0, padx=0, pady=0, sticky="ew")


	button8 = Button(gui, text='8', fg='black', bg='white',
					command=lambda: press(8), height=1, width=7)
	button8.grid(row=3, column=1, padx=0, pady=0, sticky="ew")


	button9 = Button(gui, text='9', fg='black', bg='white',
					command=lambda: press(9), height=1, width=7)
	button9.grid(row=3, column=2, padx=0, pady=0, sticky="ew")


	dvide = Button(gui, text='/', fg='black', bg='white',
					command=lambda: press("/"), height=1, width=7)
	dvide.grid(row=3, column=3, padx=0, pady=0, sticky="ew")


	# Dòng 4
	button4 = Button(gui, text='4', fg='black', bg='white',
					command=lambda: press(4), height=1, width=7)
	button4.grid(row=4, column=0, padx=0, pady=0, sticky="ew")


	button5 = Button(gui, text='5', fg='black', bg='white',
					command=lambda: press(5), height=1, width=7)
	button5.grid(row=4, column=1, padx=0, pady=0, sticky="ew")


	button6 = Button(gui, text='6', fg='black', bg='white',
					command=lambda: press(6), height=1, width=7)
	button6.grid(row=4, column=2, padx=0, pady=0, sticky="ew")


	multiply = Button(gui, text='*', fg='black', bg='white',
					command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=4, column=3, padx=0, pady=0, sticky="ew")


	# Dòng 5
	button1 = Button(gui, text='1', fg='black', bg='white',
					command=lambda: press(1), height=1, width=7)
	button1.grid(row=5, column=0, padx=0, pady=0, sticky="ew")


	button2 = Button(gui, text='2', fg='black', bg='white',
					command=lambda: press(2), height=1, width=7)
	button2.grid(row=5, column=1, padx=0, pady=0, sticky="ew")


	button3 = Button(gui, text='3', fg='black', bg='white',
					command=lambda: press(3), height=1, width=7)
	button3.grid(row=5, column=2, padx=0, pady=0, sticky="ew")


	minus = Button(gui, text='-', fg='black', bg='white',
					command=lambda: press("-"), height=1, width=7)
	minus.grid(row=5, column=3, padx=0, pady=0, sticky="ew")


	# Dòng 6
	button0 = Button(gui, text='0', fg='black', bg='white',
					command=lambda: press(0), height=1, width=7)
	button0.grid(row=6, column=0, padx=0, pady=0, sticky="ew")


	Decimal = Button(gui, text='.', fg='black', bg='white',
					command=lambda: press('.'), height=1, width=7)
	Decimal.grid(row=6, column=1, padx=0, pady=0, sticky="ew")


	equal = Button(gui, text='=', fg='black', bg='white',
					command=equalpress, height=1, width=7)
	equal.grid(row=6, column=2, padx=0, pady=0, sticky="ew")


	plus = Button(gui, text='+', fg='black', bg='white',
					command=lambda: press("+"), height=1, width=7)
	plus.grid(row=6, column=3, padx=0, pady=0, sticky="ew")

	gui.mainloop() 
