# Delima, Sheena Mae D.
# BSCPE 1-2
# May 04, 2024


# ------------------------------------------------------


# ========== PSEUDO CODE ==========
# || IMPORTS || 
from tkinter import *
from tkinter import messagebox
import pyfiglet
import sys
import time
from colorama import init, Fore, Style
import pygame
import tkinter as tk


# || ACTUAL CODES ||
# - FOR PRINTING A TEXT IN TERMINAL ONLY
# - INTRODUCTION OF THE NEO COLLBOT
init() # - Initialize

# - Code for printing the text with typewriter effect.
def printing_welcoming_remarks_with_typewriter_effect(text, delay=0.000005):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
        
text = "Welcome to Neo CollBot 🤖!"

font = pyfiglet.Figlet(font='cyberlarge') # - Choosing a fancy font.

# - Print the text with fancy font style and typewriter effect.
print(Fore.BLUE + Style.BRIGHT, end='')
printing_welcoming_remarks_with_typewriter_effect(font.renderText(text))
print(Style.RESET_ALL)

# - INFORMATION ABOUT NEO COLLBOT:
# - Typewriter effect for printing the info.
def typewriter_effect_with_color(text, delay=0.05, color='\033[1;32m'):
    for char in text:
        sys.stdout.write(color + char)  # - Set text color.
        sys.stdout.flush()
        time.sleep(delay)

# - Text to print with typewriter effect and color.
text = "Hello! My name is Neo Collins, a programmed bot. My master just created me a while ago for some purpose.\nI function as a chatbot as well as a simple calculator. Do you want to try my calculator?\n"

# - Print text with typewriter effect and color.
typewriter_effect_with_color(text)

# - Asking the user if he/she will proceed.
user_answer = input("Enter your response (y/n): ").lower()
if user_answer == "n":
    print("Thank you for your time.")
elif user_answer == "y":
    getting_ready = input("Are you now ready (y/n): ").lower()
    if getting_ready == "n":
        print("Thank you for your time.")
    elif getting_ready == "y":
        print("Let's get started!")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
else:
    print("Invalid input. Please enter 'y' or 'n'.")


# - Code for BG music.
def play_background_music(file_path):
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(-1)  
        
music_file_path = 'lofi_bg_music.mp3'
play_background_music(music_file_path)
pygame.time.delay(10)  


# =================================================================================================================


# - FOR TKINTER WINDOW
# - Root tkinter, title, and window's size.
window = Tk()
window.title("Neo Collculator 🧮")
window.geometry("500x300")


# || FUNCTION/S || 
# - Function to ask if the user wants to try again.
def ask_try_again():
    answer = messagebox.askyesno("Want to try again? 🤔", "Do you want to perform another calculation?")
    if answer:
        num1_entry_widget.delete(0, END)
        num2_entry_widget.delete(0, END)
        result_output.config(text="")
    else:
        messagebox.showinfo("Neo CollBot 🤖", "Thank you for you participation. 💖😊")
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


# - ASK THE USER FOR THE TWO NUMBERS
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


# - Tkinter mainloop
window.mainloop()
