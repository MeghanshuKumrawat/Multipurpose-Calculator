from tkinter import *

class SplitBill():
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Split bill")
        self.root.geometry("300x250")
        self.root.config(bg='black')

        # date entry
        Label(self.root, text="Amount", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=10)
        Label(self.root, text="People", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=60)
        Label(self.root, text="Split amount", bg='black', fg='#ff5d00', font=('times_new_roman 15 bold')).place(x=10, y=130)

        self.split_price = Label(self.root, text="00", bg='black', fg='white', font=('times_new_roman 15 bold'))
        self.split_price.place(x=10, y=160)

        self.amount = Entry(self.root)
        self.amount.place(x=210, y=15, width=80)
        self.people = Entry(self.root)
        self.people.place(x=240, y=65, width=50)

        # Claculate button
        Button(self.root, text="Calculate", bg="#ff5d00", command=self.calulate).place(x=10, y=210, width=280)

    def calulate(self):
        sa = int(self.amount.get()) / int(self.people.get())
        self.split_price.config(text=sa)
