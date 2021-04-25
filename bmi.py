from tkinter import *

class BMI():
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("BMI calculator")
        self.root.geometry("300x400")
        self.root.config(bg='black')

        # date entry
        Label(self.root, text="Weight (kg)", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=10)
        Label(self.root, text="Height (cm)", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=60)

        self.weight = Entry(self.root)
        self.weight.place(x=210, y=15, width=80)
        self.height = Entry(self.root)
        self.height.place(x=210, y=65, width=80)

        frame = Frame(self.root, bg='#222426', bd=1, relief=GROOVE)
        frame.place(x=10, y=180, width=280, height=160)
        Label(frame, text="BMI", bg='#222426', fg='white', font=('times_new_roman 18 bold')).place(x=220, y=50)
        Label(frame, text="Information", bg='#222426', fg='white', font=('times_new_roman 10 bold')).place(x=10, y=85)
        
        self.bmi_val = Label(frame, text="00", bg='#222426', fg='#ff5d00', font=('times_new_roman 50 bold'))
        self.bmi_val.place(x=10, y=5)  
        self.info = Label(frame, text=".....", bg='#222426', fg='#ff5d00', font=('times_new_roman 15 bold'))
        self.info.place(x=10, y=110)  

        # Claculate button
        Button(self.root, text="Calculate", bg="#ff5d00", command=self.calulate).place(x=10, y=360, width=280)

    def calulate(self):
        temp_bmi = float(self.weight.get()) / (float(self.height.get())/100)**2
        self.bmi_val.config(text=str(temp_bmi)[:5])
        if temp_bmi <= 18.4:
            self.info.config(text="You are underweight.")
        elif temp_bmi <= 24.9:
            self.info.config(text="You are healthy.")
        elif temp_bmi <= 29.9:
            self.info.config(text="You are over weight.")
        elif temp_bmi <= 34.9:
            self.info.config(text="You are severely over weight.")
        elif temp_bmi <= 39.9:
            self.info.config(text="You are obese.")
        else:
            self.info.config(text="You are severely obese.")