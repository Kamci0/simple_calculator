from engine import Engine
from tkinter import *


def click():
    calculator = Engine()
    data = user_input.get()
    calculator.get_input(data)
    if len(calculator.symbol) > 1:
        result = "Equation is to complex"
    elif len(calculator.numbers_before) < 1 or len(calculator.numbers_after) < 1:
        result = "You didn't provide enough numbers"
    elif not calculator.symbol_found:
        result = "You didn't provide a proper math symbol"
    else:
        calculator.calculate_result()
        result = calculator.get_result()
    label_result.config(text=result)


root = Tk()

# window
root.geometry("400x200")
root.config(background="#555")
root.title("Calculator")
icon = PhotoImage(file="icon.png")
root.iconphoto(True, icon)

# labels
label_about = Label(root,
                    text="Equation must have at least one and only one math symbol\nMath symbols that you can use are "
                         "- + / *\nEvery not numeric character will be ignored\nSame goes for any other non math "
                         "symbols, for example {, _ & are also ignored",
                    bg="#555",
                    fg="#fff",
                    font=("Arial", 8))

label_info = Label(root,
                   text="Enter you equation here",
                   bg="#555",
                   fg="#fff",
                   font=("Arial", 12, "bold"))

label_result = Label(root,
                     bg="#555",
                     fg="#fff",
                     font=("Arial", 12, "bold")
                     )

# buttons
calculate = Button(root,
                   text="Click to calculate",
                   font=("Arial", 9),
                   bg="#666",
                   fg="#fff",
                   activebackground="#777",
                   activeforeground="#fff",
                   command=click)

# entry's

user_input = Entry(root,
                   font="Arial")

label_info.pack()
user_input.pack()
calculate.pack()
label_result.pack()
label_about.pack()

root.mainloop()
