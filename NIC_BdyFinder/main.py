from tkinter import *
from NICfinder import *

# ---------------------- COMMANDS ----------------------

finder = NIC_finder()


def confirm():
    nic_num = number.get()
    finder.run(nic_no=nic_num)
    label_banner.configure(text=finder.banner)


def clear():
    number.delete(0, END)
    finder.reset()
    label_banner.configure(text=finder.banner)


# ------------------------- UI -------------------------


window = Tk()
window.title("Birthday finder from NIC.NO(SL)")

canvas = Canvas(width=220, height=200)
canvas.grid(column=0, row=0, rowspan=3, columnspan=2)

number = Entry(window, width=20)
number.grid(column=0, row=0, columnspan=2)

button_confirm = Button(text="Confirm", command=confirm, width=10)
button_confirm.grid(column=0, row=1)

button_clear = Button(text="Clear", command=clear, width=10)
button_clear.grid(column=1, row=1)

label_banner = Label(text=f"Your Birth Year is: \nYour Birth Month is: \nYour Birth date is: \nYou are a: ",
                     justify="left")
label_banner.grid(column=0, row=2, columnspan=2, sticky="w", padx=10, pady=10)

window.mainloop()
