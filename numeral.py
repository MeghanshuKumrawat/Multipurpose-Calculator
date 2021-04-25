from tkinter import *
from tkinter import ttk, messagebox

class Numeral():
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Numeral calculator")
        self.root.geometry("300x230")
        self.root.config(bg='black')

        # date entry
        self.num_from = ttk.Combobox(self.root, state='readonly')
        self.num_from.place(x=10, y=10)
        self.num_from['values'] = ['Binary_BIN', 'Octal_OCT', 'Decimal_DEC', 'Hexadecimal_HEX']

        Label(self.root, text="To", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=60, y=35)

        self.num_to = ttk.Combobox(self.root, state='readonly')
        self.num_to.place(x=10, y=70)
        self.num_to['values'] = ['Binary_BIN', 'Octal_OCT', 'Decimal_DEC', 'Hexadecimal_HEX']

        self.num = Entry(self.root)
        self.num.place(x=210, y=10, width=80)
        self.result_label = Label(self.root, text="00", bg='black', fg='#ff5d00', font=('times_new_roman 15 bold'))
        self.result_label.place(x=180, y=70, width=80)

        Label(self.root, text="Result : ", bg='black', fg='#ff5d00', font=('times_new_roman 15 bold')).place(x=10, y=130)
        self.result = Label(self.root, text="0", bg='black', fg='#ff5d00', font=('times_new_roman 15 bold'))
        self.result.place(x=90, y=130)

        # Claculate button
        Button(self.root, text="Calculate", bg="#ff5d00", command=self.calculate).place(x=10, y=190, width=280)

    def calculate(self):
        function_name = self.num_from.get() + '_to_' + self.num_to.get()
        if function_name == "Binary_BIN_to_Binary_BIN" or function_name == "Octal_OCT_to_Octal_OCT" or function_name == "Decimal_DEC_to_Decimal_DEC" or function_name == "Hexadecimal_HEX_to_Hexadecimal_HEX":
            messagebox.showerror("Numeral calculator", "This method is allowed!!!\nPlease select different parameters.")
        elif self.num_from.get() == '' or self.num_to.get() == '':
            messagebox.showinfo('Numeral calculator', 'Please select some parameters.')
        elif self.num.get() == '':
            messagebox.showinfo('Numeral calculator', 'Please enter some number in the entry box.')
        else:
            result = eval('self.' + function_name + '()')
            self.result.config(text=result)
            self.result_label.config(text=result)

    def Binary_BIN_to_Octal_OCT(self):
        temp = int(self.num.get(),2)
        return oct(temp)
    def Binary_BIN_to_Decimal_DEC(self):
        temp = int(self.num.get(),2)
        return temp
    def Binary_BIN_to_Hexadecimal_HEX(self):
        temp = int(self.num.get(),2)
        return hex(temp)

    def Octal_OCT_to_Binary_BIN(self):
        temp = int(self.num.get(),8)
        return bin(temp)
    def Octal_OCT_to_Decimal_DEC(self):
        temp = int(self.num.get(),8)
        return temp
    def Octal_OCT_to_Hexadecimal_HEX(self):
        temp = int(self.num.get(),8)
        return hex(temp)

    def Decimal_DEC_to_Binary_BIN(self):
        n = int(self.num.get())
        return bin(n)
    def Decimal_DEC_to_Octal_OCT(self):
        n = int(self.num.get())
        return oct(n)
    def Decimal_DEC_to_Hexadecimal_HEX(self):
        n = int(self.num.get())
        return hex(n)

    def Hexadecimal_HEX_to_Binary_BIN(self):
        temp = int(self.num.get(),8)
        return bin(temp)
    def Hexadecimal_HEX_to_Octal_OCT(self):
        temp = int(self.num.get(),8)
        return oct(temp)
    def Hexadecimal_HEX_to_Decimal_DEC(self):
        temp = int(self.num.get(),8)
        return temp

