# Delima, Sheena Mae D.
# BSCPE 1-2
# May 04, 2024


# ------------------------------------------------------


# ========== PSEUDO CODE ==========
# || LIBRARIES \ PACKAGERS ||

# || IMPORTS || 
from tkinter import *

# || ACTUAL CODES ||
# - Root tkinter, title, and window's size
window = Tk()
window.title("Calculator")
window.geometry("500x300")

# - ASK THE USER FOR THE TWO NUMBERS.
# - Creating the label 1 and entry 1 for user to input his/her desired number.
num1 = Label(window, text = "Enter your first number:", font=("Arial", 15))
num1.pack()
num1_entry_widget = Entry(window, font=("Helvetica", 12))
num1_entry_widget.pack()

# - Creating the label 2 and entry 2 for user to input his/her desired number.
num2 = Label(window, text = "Enter your first number:", font=("Arial", 15))
num2.pack()
num2_entry_widget = Entry(window, font=("Helvetica", 12))
num2_entry_widget.pack()


# - ASK USER FOR THE OPERATION
# - # - Creating the label 1 and entry 1 for user to input his/her desired number.
button_label = Label(window, text = "What operation do you want to use?", font=("Arial", 15))
button_label.pack()


# - Try and except category.
# - If,elif,else code.
# - Tkinter mainloop
window.mainloop()