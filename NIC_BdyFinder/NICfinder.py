from tkinter import messagebox


class NIC_finder:

    def __init__(self):
        self.banner = "Your Birth Year is: \nYour Birth Month is: \nYour Birth date is: \nYou are a: "
        self.year = None
        self.month = None
        self.date = None
        self.gender = None
        self.day_num = None

    def check_leap(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def nic(self):
        self.date_and_month()

        if self.year and self.month and self.date and self.gender:
            self.banner = f"Your Birth Year is:\t\t{self.year}\nYour Birth Month is:\t{self.month}\n" \
                          f"Your Birth date is:\t\t{self.date}\nYou are a:\t\t{self.gender}"
        else:
            messagebox.showerror(title="ERROR", message="Enter a valid NIC number")
            self.reset()

    def date_and_month(self):

        if self.day_num > 500:
            day = self.day_num - 500
            self.gender = "Female"
        else:
            day = self.day_num
            self.gender = "Male"

        if 0 < day <= 31:
            self.month = "January"
            self.date = day
        elif 31 < day <= 59:
            self.month = "February"
            self.date = day - 31
        elif 59 < day <= 90:
            self.month = "March"
            self.date = day - 59
        elif 90 < day <= 120:
            self.month = "April"
            self.date = day - 90
        elif 120 < day <= 151:
            self.month = "May"
            self.date = day - 120
        elif 151 < day <= 181:
            self.month = "June"
            self.date = day - 151
        elif 181 < day <= 212:
            self.month = "July"
            self.date = day - 181
        elif 212 < day <= 243:
            self.month = "August"
            self.date = day - 212
        elif 243 < day <= 273:
            self.month = "September"
            self.date = day - 243
        elif 273 < day <= 304:
            self.month = "October"
            self.date = day - 273
        elif 304 < day <= 334:
            self.month = "November"
            self.date = day - 304
        elif 334 < day <= 365:
            self.month = "December"
            self.date = day - 334
        else:
            self.month = None
            self.date = None

    def run(self, nic_no):
        if len(nic_no) == 10:
            self.year = 1900 + int(nic_no[0:2])
            self.day_num = int(nic_no[2:5]) - 1
            self.nic()
        elif len(nic_no) == 12:
            self.year = int(nic_no[0:4])
            self.day_num = int(nic_no[4:7]) - 1
            self.nic()
        else:
            messagebox.showerror(title="ERROR", message="Enter a valid NIC number")
            self.reset()

    def reset(self):
        self.year = ""
        self.month = ""
        self.date = ""
        self.gender = ""
        self.banner = "Your Birth Year is: \nYour Birth Month is: \nYour Birth date is: \nYou are a: "
