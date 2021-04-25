from tkinter import *
from tkcalendar import DateEntry

class Percentage():
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Percentage calculator")
        self.root.geometry("300x250")
        self.root.config(bg='black')

        # date entry
        Label(self.root, text="Percentage (%)", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=10)
        Label(self.root, text="Total", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=60)
        Label(self.root, text="Result", bg='black', fg='#ff5d00', font=('times_new_roman 15 bold')).place(x=10, y=130)
        self.result = Label(self.root, text="00", bg='black', fg='#ff5d00', font=('times_new_roman 15 bold'))
        self.result.place(x=230, y=130)

        self.percentage = Entry(self.root)
        self.percentage.place(x=240, y=15, width=50)
        self.total = Entry(self.root)
        self.total.place(x=210, y=65, width=80)

        # Claculate button
        Button(self.root, text="Calculate", bg="#ff5d00", command=self.calulate).place(x=10, y=210, width=280)

    def calulate(self):
        fp = (int(self.total.get()) * int(self.percentage.get()) / 100)
        self.result.config(text=fp)
