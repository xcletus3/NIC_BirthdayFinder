from tkinter import messagebox


class NIC_finder:

    def __init__(self):
        self.banner = None
        self.year = None
        self.month = None
        self.date = None
        self.gender = None
        self.day_num = None

    # validate and output
    def nic(self):
        self.date_and_month()

        if self.year and self.month and self.date and self.gender:
            self.banner = f"Your Birth Year is:\t\t{self.year}\nYour Birth Month is:\t{self.month}\n" \
                          f"Your Birth date is:\t\t{self.date}\nYou are a:\t\t{self.gender}"
        else:
            messagebox.showerror(title="ERROR", message="Enter a valid NIC number")
            self.reset()

    def date_and_month(self):

        # Checking the gender
        if self.day_num > 500:
            day = self.day_num - 500
            self.gender = "Female"
        else:
            day = self.day_num
            self.gender = "Male"

        # Checking the date and month of birth
        if 0 < day <= 31:
            self.month = "January"
            self.date = day
        elif 31 < day <= 60:
            self.month = "February"
            self.date = day - 31
        elif 60 < day <= 91:
            self.month = "March"
            self.date = day - 60
        elif 91 < day <= 121:
            self.month = "April"
            self.date = day - 91
        elif 121 < day <= 152:
            self.month = "May"
            self.date = day - 121
        elif 152 < day <= 182:
            self.month = "June"
            self.date = day - 152
        elif 182 < day <= 213:
            self.month = "July"
            self.date = day - 182
        elif 213 < day <= 244:
            self.month = "August"
            self.date = day - 213
        elif 244 < day <= 274:
            self.month = "September"
            self.date = day - 244
        elif 274 < day <= 305:
            self.month = "October"
            self.date = day - 274
        elif 305 < day <= 335:
            self.month = "November"
            self.date = day - 305
        elif 335 < day <= 366:
            self.month = "December"
            self.date = day - 335
        else:
            self.month = None
            self.date = None

    # Run the programme
    def run(self, nic_no):
        if len(nic_no) == 10:
            self.year = 1900 + int(nic_no[0:2])
            self.day_num = int(nic_no[2:5])
            self.nic()
        elif len(nic_no) == 12:
            self.year = int(nic_no[0:4])
            self.day_num = int(nic_no[4:7])
            self.nic()
        else:
            messagebox.showerror(title="ERROR", message="Enter a valid NIC number")
            self.reset()

    # Reset the UI
    def reset(self):
        self.year = ""
        self.month = ""
        self.date = ""
        self.gender = ""
        self.banner = "Your Birth Year is: \nYour Birth Month is: \nYour Birth date is: \nYou are a: "
