from tkinter import *
from tkcalendar import DateEntry

class Date():
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Date calculator")
        self.root.geometry("300x430")
        self.root.config(bg='black')
        self.cake = PhotoImage(file='cake.png')

        # date entry
        Label(self.root, text="From", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=10)
        Label(self.root, text="To", bg='black', fg='white', font=('times_new_roman 15 bold')).place(x=10, y=60)
        self.date_from = DateEntry(self.root, background='black')
        self.date_from.place(x=200, y=15)
        self.date_to = DateEntry(self.root, background='black')
        self.date_to.place(x=200, y=65)

        # Claculate button
        Button(self.root, text="Calculate", bg="#ff5d00", command=self.calculate).place(x=10, y=110, width=280)

        # main result frame
        result_frame = Frame(self.root, bg='#222426')
        result_frame.place(x=10, y=150, width=280, height=260)
        Label(result_frame, text="Difference", bg='#222426', fg='#ff5d00', font=('arial 20 bold')).place(x=70, y=10)


        # sub frame 3 for Summary section
        Difference_frame = Frame(result_frame, bg='#222426', bd=1, relief=GROOVE)
        Difference_frame.place(x=0, y=60, width=280, height=90)
        Label(Difference_frame, text="Years", bg='#222426', fg='white', font=('arial 10')).place(x=20, y=20)
        Label(Difference_frame, text="Months", bg='#222426', fg='white', font=('arial 10')).place(x=100, y=20)
        Label(Difference_frame, text="Days", bg='#222426', fg='white', font=('arial 10')).place(x=190, y=20)

        self.summary_year = Label(Difference_frame, text="00", bg='#222426', fg='white', font=('arial 15 bold'))
        self.summary_year.place(x=20, y=40)
        self.summary_month = Label(Difference_frame, text="00", bg='#222426', fg='white', font=('arial 15 bold'))
        self.summary_month.place(x=100, y=40)
        self.summary_days = Label(Difference_frame, text="00", bg='#222426', fg='white', font=('arial 15 bold'))
        self.summary_days.place(x=190, y=40)

        # sub frame 1 for Age section
        From_frame = Frame(result_frame, bg='#222426')
        From_frame.place(x=0, y=160, width=140, height=100)
        Label(From_frame, text="From", bg='#222426', fg='#ff5d00', font=('arial 20 bold')).place(x=30, y=20)
        self.from_date = Label(From_frame, text=self.date_from.get_date(), bg='#222426', fg='white',
                                         font=('arial 10 bold'))
        self.from_date.place(x=30, y=55)

        # sub frame 2 for Next birthday section
        To_frame = Frame(result_frame, bg='#222426')
        To_frame.place(x=140, y=160, width=140, height=100)
        Label(To_frame, text="To", bg='#222426', fg='#ff5d00', font=('arial 20 bold')).place(x=45, y=20)
        self.to_date = Label(To_frame, text=self.date_to.get_date(), bg='#222426', fg='white', font=('arial 10 bold'))
        self.to_date.place(x=30, y=55)



    def calculate(self):
        import datetime
        now = datetime.datetime.now()
        current = self.date_to.get_date()
        birth = self.date_from.get_date()

        current_date = datetime.datetime.strptime(str(current), '%Y-%m-%d')
        birth_date = datetime.datetime.strptime(str(birth), '%Y-%m-%d')

        days_left = current_date - birth_date

        years = ((days_left.total_seconds())/(365.242*24*3600))
        years_int = int(years)
        months = (years - years_int)*12
        months_int = int(months)
        days = (months - months_int)*(365.242/12)
        days_int = int(days)
        # uncomment this if you want to add seconds
        # hours = (days - days_int)*24
        # hours_int = int(hours)
        # minutes = (hours - hours_int)*60
        # minutes_int = int(minutes)
        # seconds = (minutes - minutes_int)*60

        self.summary_year.config(text=years_int)
        self.summary_month.config(text=months_int)
        self.summary_days.config(text=days_int)
        self.from_date.config(text=self.date_from.get_date())
        self.to_date.config(text=self.date_to.get_date())

# WARNING :- if your birth date is before 2000, do not use date picker, Enter the date manually