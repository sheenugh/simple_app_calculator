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
num1 = Label(window, text = "Enter your first number:", font=("times", 18))
num1.pack()
num1_entry_widget = Entry(window, font=("Helvetica", 12))
num1_entry_widget.pack()

# - Creating the label 2 and entry 2 for user to input his/her desired number.
num2 = Label(window, text = "Enter your first number:", font=("times", 18))
num2.pack()
num2_entry_widget = Entry(window, font=("Helvetica", 12))
num2_entry_widget.pack()

# - ASK USER FOR THE OPERATION
# - Creating a label for asking the user of his/her desired operation.
button_label = Label(window, text = "What operation do you want to use?", font=("times", 17))
button_label.pack()

# - BUTTON FOR OPERATIONS
frame = Frame(window) 
frame.pack(pady=10, padx=10)
# - Addition button.
addition_button =Button(frame, text="Addition", font=("serif", 11))
addition_button.pack(side=LEFT, padx=8)
# - Subtraction button.
subtraction_button =Button(frame, text="Subtraction", font=("serif", 11))
subtraction_button.pack(side=LEFT, padx=8)
# - Multiplication button.
multiplication_button =Button(frame, text="Multiplication", font=("serif", 11))
multiplication_button.pack(side=LEFT, padx=8)
# - Division button.
division_button =Button(frame, text="Division", font=("serif", 11))
division_button.pack(side=LEFT, padx=8)

# - RESULT LABEL AND ENTRY
# - Result label.
result_label = Label(window, text="Result", font=('times', 18))
result_label.pack()

result_output = Label(window, bg="White", width=20, font=("Helvetica", 12), relief="sunken", background="lightgray")
result_output.pack()

# - Try and except category.
# - If,elif,else code.
# - Tkinter mainloop
window.mainloop()