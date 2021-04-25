from tkinter import *
from tkcalendar import DateEntry

class Discount():
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Discount calculator")
        self.root.geometry("300x250")
        self.root.config(bg='black')

        # date entry
        Label(self.root, text="Original price", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=10)
        Label(self.root, text="Discount (% off)", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=60)
        Label(self.root, text="Final price", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=110)
        self.final_price = Label(self.root, text="00", bg='black', fg='white', font=('times_new_roman 15 bold'))
        self.final_price.place(x=220, y=110)
        self.save_price = Label(self.root, text="You save : 00", bg='black', fg='#ff5d00', font=('times_new_roman 15 bold'))
        self.save_price.place(x=70, y=160)

        self.original_price = Entry(self.root)
        self.original_price.place(x=210, y=15, width=80)
        self.discount = Entry(self.root)
        self.discount.place(x=240, y=65, width=50)

        # Claculate button
        Button(self.root, text="Calculate", bg="#ff5d00", command=self.calulate).place(x=10, y=210, width=280)

    def calulate(self):
        fp = int(self.original_price.get()) - (int(self.original_price.get()) * int(self.discount.get()) / 100)
        s = int(self.original_price.get()) - fp
        print(type(fp))
        self.final_price.config(text=fp)
        self.save_price.config(text='You save : ' + str(s))
