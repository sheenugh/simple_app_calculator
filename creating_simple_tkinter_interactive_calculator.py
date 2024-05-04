# Delima, Sheena Mae D.
# BSCPE 1-2
# May 04, 2024


# ------------------------------------------------------


# ========== PSEUDO CODE ==========
# || IMPORTS || 
from tkinter import *
from tkinter import messagebox
import pyfiglet
import time
from colorama import init, Fore, Style



# || ACTUAL CODES ||
# - Introduction code.

# - Information about Neo_Collbot

# - Root tkinter, title, and window's size
window = Tk()
window.title("Neo_Collculator 🧮")
window.geometry("500x300")

# || FUNCTION/S || 
# - Function to ask if the user wants to try again
def ask_try_again():
    answer = messagebox.askyesno("Want to try again? 🤔", "Do you want to perform another calculation?")
    if answer:
        num1_entry_widget.delete(0, END)
        num2_entry_widget.delete(0, END)
        result_output.config(text="")
    else:
        messagebox.showinfo("Neo_Collbot 🤖", "Thank you for you participation. 💖😊")
        window.destroy()
        
# - Try and except category.
def calculation(option): 
    try:
        number1_inputted_value = float(num1_entry_widget.get())
        number2_inputted_value = float(num2_entry_widget.get())
        # - If,elif,else code.
        if (option == "+"):
            result = number1_inputted_value + number2_inputted_value
        elif (option == "-"):
            result = number1_inputted_value - number2_inputted_value
        elif (option == "*"):
            result = number1_inputted_value * number2_inputted_value
        elif (option == "/"):
            result = number1_inputted_value / number2_inputted_value
        else:
            pass
            return
            
        rounded_off_result = round(result, 2)
        result_output.config(text=str(rounded_off_result))
        
        ask_try_again()
        
    except ValueError: 
        messagebox.showerror("Error", "Please input 'any number' only 😊")
    
    except:
        messagebox.showerror("Error", "Oops! Something went wrong. Please check your input and try again 😉")

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
button_label = Label(window, text = "Choose the operation you want to use", font=("times", 17))
button_label.pack()

# - BUTTON FOR OPERATIONS
frame = Frame(window) 
frame.pack(pady=10, padx=10)
# - Addition button.
addition_button =Button(frame, text="Addition", font=("serif", 11), command=lambda:calculation("+"))
addition_button.pack(side=LEFT, padx=8)
# - Subtraction button.
subtraction_button =Button(frame, text="Subtraction", font=("serif", 11),  command=lambda:calculation("-"))
subtraction_button.pack(side=LEFT, padx=8)
# - Multiplication button.
multiplication_button =Button(frame, text="Multiplication", font=("serif", 11),  command=lambda:calculation("*"))
multiplication_button.pack(side=LEFT, padx=8)
# - Division button.
division_button =Button(frame, text="Division", font=("serif", 11),  command=lambda:calculation("/"))
division_button.pack(side=LEFT, padx=8)

# - RESULT LABEL AND ENTRY
# - Result label.
result_label = Label(window, text="Result", font=('times', 18))
result_label.pack()

result_output = Label(window, bg="White", width=20, font=("Helvetica", 12), relief="sunken", background="lightgray")
result_output.pack()

# - Asking the user if he/she wants to try again.


# - Tkinter mainloop
window.mainloop()