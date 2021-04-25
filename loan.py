from tkinter import *

class LoanCalculator():
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Loan calculator")
        self.root.geometry("300x400")
        self.root.config(bg='black')

        # date entry
        Label(self.root, text="Principal", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=10)
        Label(self.root, text="Interest (%)", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=60)
        Label(self.root, text="Loan tenure", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=110)

        self.principal = Entry(self.root)
        self.principal.place(x=210, y=15, width=80)
        self.interest = Entry(self.root)
        self.interest.place(x=210, y=65, width=80)
        self.year = Entry(self.root)
        self.year.place(x=210, y=115, width=80)

        frame = Frame(self.root, bg='#222426', bd=1, relief=GROOVE)
        frame.place(x=10, y=180, width=280, height=160)
        Label(frame, text="Monthly payment", bg='#222426', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=10)
        Label(frame, text="Total payment", bg='#222426', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=80)
        
        self.monthly_price = Label(frame, text="00", bg='#222426', fg='#ff5d00', font=('times_new_roman 15 bold'))
        self.monthly_price.place(x=10, y=40)  
        self.total_price = Label(frame, text="00", bg='#222426', fg='#ff5d00', font=('times_new_roman 15 bold'))
        self.total_price.place(x=10, y=110)  

        # Claculate button
        Button(self.root, text="Calculate", bg="#ff5d00", command=self.calulate).place(x=10, y=360, width=280)

    def calulate(self):
        principal=float(self.principal.get())
        interest=float(self.interest.get())/100/12
        year=int(self.year.get())*12
        monthly_p = principal*(interest*(1+interest)**year)/((1+interest)**year-1)
        self.monthly_price.config(text=monthly_p)

        total_p = monthly_p * year
        self.total_price.config(text=total_p)