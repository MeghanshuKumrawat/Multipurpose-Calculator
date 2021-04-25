from tkinter import *
from tkinter import ttk, messagebox

class Temperature():
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Temperature calculator")
        self.root.geometry("300x230")
        self.root.config(bg='black')

        # date entry
        self.temp_from = ttk.Combobox(self.root, state='readonly')
        self.temp_from.place(x=10, y=10)
        self.temp_from['values'] = ['Celsius', 'Fahrenheit', 'Kelvin']

        Label(self.root, text="To", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=60, y=35)

        self.temp_to = ttk.Combobox(self.root, state='readonly')
        self.temp_to.place(x=10, y=70)
        self.temp_to['values'] = ['Celsius', 'Fahrenheit', 'Kelvin']

        self.temp_1 = Entry(self.root)
        self.temp_1.place(x=210, y=10, width=80)
        self.result_label = Label(self.root, text="00", bg='black', fg='#ff5d00', font=('times_new_roman 15 bold'))
        self.result_label.place(x=180, y=70, width=80)

        Label(self.root, text="Result : ", bg='black', fg='#ff5d00', font=('times_new_roman 15 bold')).place(x=10, y=130)
        self.result = Label(self.root, text="0", bg='black', fg='#ff5d00', font=('times_new_roman 15 bold'))
        self.result.place(x=90, y=130)

        # Claculate button
        Button(self.root, text="Calculate", bg="#ff5d00", command=self.calculate).place(x=10, y=190, width=280)

    def calculate(self):
        function_name = self.temp_from.get() + "_to_" + self.temp_to.get()
        if function_name == 'Fahrenheit_to_Fahrenheit' or function_name == 'Celsius_to_Celsius' or function_name == 'Kelvin_to_Kelvin':
            messagebox.showerror("Temperature calculator", "This method is allowed!!!\nPlease select different parameters.")
        elif self.temp_from.get() == '' or self.temp_to.get() == '':
            messagebox.showinfo('Numeral calculator', 'Please select some parameters.')
        elif self.temp_1.get() == '':
            messagebox.showinfo('Numeral calculator', 'Please enter some number in the entry box.')
        else:
            result = eval('self.' + function_name + '()')
            self.result.config(text=result)
            self.result_label.config(text=result)

    def Fahrenheit_to_Celsius(self):
        print('Fahrenheit_to_Celsius pahuch gaya')
        f = int(self.temp_1.get())
        c = (f - 32) * 5.0/9.0
        return c
    def Fahrenheit_to_Kelvin(self):
        print('Fahrenheit_to_Kelvin pahuch gaya')
        f = int(self.temp_1.get())
        k = 273.5 + ((f - 32.0) * (5.0/9.0))
        return k

    def Kelvin_to_Celsius(self):
        print('Kelvin_to_Celsius pahuch gaya')
        k = int(self.temp_1.get())
        c = (k - 273.15)
        return c
    def Kelvin_to_Fahrenheit(self):
        print('Kelvin_to_Fahrenheit pahuch gaya')
        k = int(self.temp_1.get())
        c = (k - 273.15)
        f = c*(9/5)+32
        return f

    def Celsius_to_Fahrenheit(self):
        print('Celsius_to_Fahrenheit pahuch gaya')
        c = int(self.temp_1.get())
        f = 9.0/5.0 * c +32
        return f
    def Celsius_to_Kelvin(self):
        print('Celsius_to_Kelvin pahuch gaya')
        c = int(self.temp_1.get())
        k = (c + 273.15)
        return k
