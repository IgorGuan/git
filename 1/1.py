import tkinter as tk
from tkinter import simpledialog, messagebox

def is_palindrome(s):
    cleaned_string = ''.join(s.lower().split())
    return cleaned_string == cleaned_string[::-1]

# Create the main window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Pop up the input dialog
input_string = simpledialog.askstring("Input", "Please enter a string:")

if input_string is not None:  # Check if the user entered a string
    if is_palindrome(input_string):
        messagebox.showinfo("Result", f'"{input_string}" is a palindrome.')
    else:
        messagebox.showinfo("Result", f'"{input_string}" is not a palindrome.')
else:
    messagebox.showinfo("Result", "No string was entered.")

# End the program
root.destroy()
