from tkinter import *
from tkinter import ttk
from age import Age
from date import Date
from discount import Discount
from numeral import Numeral
from percentage import Percentage
from temperature import Temperature
from loan import LoanCalculator
from split_bill import SplitBill
from bmi import BMI

class Calculator():
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("450x600")
        self.root.maxsize(450,600)
        self.expression = ""

        calculator = Frame(root, bg='black')
        calculator.place(x=0, y=0, width=450, height=600)
        conversion = Frame(root, bg='black')
        conversion.place(x=460, y=0, width=350, height=600)
        

        Label(calculator, text="Standard", bg="black", fg="white", bd=1, relief=SOLID, font=('arial', 20, 'bold')).place(x=10, y=10)
        self.equation = Label(calculator, text="0", bg="black", fg='#ff5d00', font=('arial', 20, 'bold'))
        self.equation.place(x=20, y=100)
        self.result = Label(calculator, text="0", bg="black", fg='white', font=('arial', 40, 'bold'))
        self.result.place(x=20, y=140)

        btn_conversion_open = Button(calculator, width=5, height=0, font=('arial', 15, 'bold'), text=">>>", bg="black", activebackground="white",
                         activeforeground="white", fg="White", command=self.conversion_open).place(x=375, y=5)
        btn_conversion_close = Button(conversion, width=5, height=0, font=('arial', 15, 'bold'), text="X", bg="black", activebackground="white",
                         activeforeground="white", fg="red", command=self.conversion_close).place(x=265, y=5)

        btn_ce = Button(calculator, width=15, height=4, text="CE", bg="#ff5d00", activebackground="white",
                         activeforeground="white", fg="White", command=lambda: self.press("CE")).place(x=0, y=250)
        btn_7 = Button(calculator, width=15, height=4, text="7", bg="black", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("7")).place(x=0, y=320)
        btn_4 = Button(calculator, width=15, height=4, text="4", bg="black", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("4")).place(x=0, y=390)
        btn_1 = Button(calculator, width=15, height=4, text="1", bg="black", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("1")).place(x=0, y=460)
        btn_ex = Button(calculator, width=15, height=4, text="00", bg="black", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("00")).place(x=0, y=530)
        btn_c = Button(calculator, width=15, height=4, text="C", bg="#ff5d00", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("C")).place(x=114, y=250)
        btn_8 = Button(calculator, width=15, height=4, text="8", bg="black", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("8")).place(x=114, y=320)
        btn_5 = Button(calculator, width=15, height=4, text="5", bg="black", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("5")).place(x=114, y=390)
        btn_2 = Button(calculator, width=15, height=4, text="2", bg="black", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("2")).place(x=114, y=460)
        btn_0 = Button(calculator, width=15, height=4, text="0", bg="black", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("0")).place(x=114, y=530)
        btn_back = Button(calculator, width=15, height=4, text="| X", bg="#ff5d00", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("X")).place(x=228, y=250)
        btn_9 = Button(calculator, width=15, height=4, text="9", bg="black", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("9")).place(x=228, y=320)
        btn_6 = Button(calculator, width=15, height=4, text="6", bg="black", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("6")).place(x=228, y=390)
        btn_3 = Button(calculator, width=15, height=4, text="3", bg="black", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("3")).place(x=228, y=460)
        btn_dot = Button(calculator, width=15, height=4, text=".", bg="black", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press(".")).place(x=228, y=530)
        btn_divide = Button(calculator, width=15, height=4, text="/", bg="#ff5d00", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("/")).place(x=342, y=250)
        btn_multiply = Button(calculator, width=15, height=4, text="*", bg="#ff5d00", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("*")).place(x=342, y=320)
        btn_minus = Button(calculator, width=15, height=4, text="-", bg="#ff5d00", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("-")).place(x=342, y=390)
        btn_plus = Button(calculator, width=15, height=4, text="+", bg="#ff5d00", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("+")).place(x=342, y=460)
        btn_equal = Button(calculator, width=15, height=4, text="=", bg="#ff5d00", activebackground="light blue",
                          activeforeground="white", fg="White", command=lambda: self.press("=")).place(x=342, y=530)
        
        Label(conversion, text="Conversion", bg="black", fg="white", bd=1, relief=SOLID, font=('arial', 20, 'bold')).place(x=10, y=10)
        self.btn_age = Button(conversion, width=12, height=3, text="Age", bg="#ff5d00", activebackground="light blue",
                          font=('arial', 15, 'bold'), activeforeground="white", fg="White", command=lambda:Age(root)).place(x=10, y=100)
        btn_date = Button(conversion, width=12, height=3, text="Date", bg="#ff5d00", activebackground="light blue",
                          font=('arial', 15, 'bold'), activeforeground="white", fg="White", command=lambda:Date(root)).place(x=175, y=100)
        btn_discount = Button(conversion, width=12, height=3, text="Discount", bg="#ff5d00", activebackground="light blue",
                          font=('arial', 15, 'bold'), activeforeground="white", fg="White", command=lambda:Discount(root)).place(x=10, y=200)
        btn_numeral = Button(conversion, width=12, height=3, text="Numeral", bg="#ff5d00", activebackground="light blue",
                          font=('arial', 15, 'bold'), activeforeground="white", fg="White", command=lambda:Numeral(root)).place(x=175, y=200)
        btn_percentage = Button(conversion, width=12, height=3, text="Percentage", bg="#ff5d00", activebackground="light blue",
                          font=('arial', 15, 'bold'), activeforeground="white", fg="White", command=lambda:Percentage(root)).place(x=10, y=300)
        btn_temperature = Button(conversion, width=12, height=3, text="Temperature", bg="#ff5d00", activebackground="light blue",
                          font=('arial', 15, 'bold'), activeforeground="white", fg="White", command=lambda:Temperature(root)).place(x=175, y=300)
        btn_bmi = Button(conversion, width=12, height=3, text="BMI", bg="#ff5d00", activebackground="light blue",
                          font=('arial', 15, 'bold'), activeforeground="white", fg="White", command=lambda:BMI(root)).place(x=10, y=400)
        btn_loan = Button(conversion, width=12, height=3, text="Loan", bg="#ff5d00", activebackground="light blue",
                          font=('arial', 15, 'bold'), activeforeground="white", fg="White", command=lambda:LoanCalculator(root)).place(x=175, y=400)
        btn_split_bill = Button(conversion, width=12, height=3, text="Split bill", bg="#ff5d00", activebackground="light blue",
                          font=('arial', 15, 'bold'), activeforeground="white", fg="White", command=lambda:SplitBill(root)).place(x=10, y=500)
        btn_exit = Button(conversion, width=12, height=3, text="EXIT", bg="black", activebackground="light blue",
                          font=('arial', 15, 'bold'), activeforeground="white", fg="White", command=root.destroy).place(x=175, y=500)
    
    def press(self, num):
        if num == "X":
            self.expression = self.expression[:-1]
            self.result.config(text=self.expression)
        elif num == "CE" or num == "C":
            self.expression = ""
            self.result.config(text=0)
            self.equation.config(text=0)
        elif num == "=":
            try:
                self.equation.config(text=self.expression)
                self.result.config(text=str(eval(self.expression)))
            except:
                self.result.config(text="error")
        else:
            self.expression += num
            self.result.config(text=self.expression)

    def conversion_open(self):
        self.root.geometry('800x600')
        self.root.maxsize(800,600)

    def conversion_close(self):
        self.root.geometry('450x600')
        self.root.maxsize(450,600)

root = Tk()
obj = Calculator(root)
root.mainloop()
