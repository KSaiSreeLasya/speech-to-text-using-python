import tkinter as tk
from tkinter import messagebox
import os
import openpyxl

import subprocess
import sys
from tkinter import Label, Frame, Canvas
from PIL import Image, ImageTk
def register():
    root.destroy()
    subprocess.Popen([sys.executable, "reg.py"])

from tkinter import messagebox
import os

def login():
    username = entry1.get()
    password = entry2.get()

    if not username or not password:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        # Open the Excel file to check credentials
        wb = openpyxl.load_workbook('registration_data.xlsx')

        # Select the active sheet (the one where registration data is stored)
        sheet = wb.active

        # Loop through each row to find matching username and password
        for row in range(2, sheet.max_row + 1):  # Start from row 2 to skip headers
            stored_username = sheet[f'A{row}'].value  # Username in column A
            stored_password = sheet[f'C{row}'].value  # Password in column C

            if username == stored_username and password == stored_password:
                messagebox.showinfo("Login", "Login Successful")
                root.destroy()  # Close the login window
                os.system('python speech.py')  # Launch speech.py (ensure it's in the same directory)
                return

        # If no match is found
        messagebox.showerror("Login", "Invalid Credentials")

    except FileNotFoundError:
        messagebox.showerror("Error", "No registration data found!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


root = tk.Tk()
root.title("Vocal Script - Home Page")
root.geometry("1366x768")

# Load and set the background image
bg_image = Image.open("bg1.jpg")  # Replace with your image path
bg_image = bg_image.resize((1550, 780), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Canvas and add the background image
canvas = Canvas(root, width=1550, height=780)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=bg_photo)

# Prevent white space by resizing dynamically
def resize_image(event):
    new_width = event.width
    new_height = event.height
    resized_image = bg_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    updated_bg_photo = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, anchor="nw", image=updated_bg_photo)
    canvas.image = updated_bg_photo  # Keep a reference to avoid garbage collection

# Bind resizing events
root.bind("<Configure>", resize_image)

# Header Frame
header_frame = Frame(root, bg="#1f1c2c", height=150)
header_frame.place(x=0, y=0, relwidth=1)

# Load and resize the logo
original_logo = Image.open("hlogo.png")
resized_logo = original_logo.resize((130, 130), Image.Resampling.LANCZOS)
logo_image = ImageTk.PhotoImage(resized_logo)

# Place logo in the header frame
logo_label = Label(header_frame, image=logo_image, bg="#2c2738")
logo_label.place(x=20, y=10)

# Header Label
header_label = tk.Label(header_frame, text=" Vocal Script", font=('Helvetica', 32, 'bold'), bg="#1f1c2c", fg="#ffffff", pady=10)
header_label.place(x=180, y=37)

# Caption Label
caption_label = Label(header_frame, text="  Say It Once, Keep It Forever!", font=("Helvetica", 15, "italic"), fg="white", bg="#1f1c2c")
caption_label.place(x=188, y=93)

# Frame for the login form
form_frame = tk.Frame(root, bg="#1f1c2c", padx=20, pady=20, relief="raised", borderwidth=3)
form_frame.place(relx=0.5, rely=0.5, anchor="center")

heading_label = tk.Label(form_frame, text="Login", font=("Helvetica", 20, "bold"), bg="#1f1c2c", fg="white")
heading_label.grid(row=0, column=0, columnspan=2, pady=10)
# Username Label and Entry
label1 = tk.Label(form_frame, text="Username:", font=("Arial", 16, "bold"), bg="#1f1c2c", fg="white")
label1.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry1 = tk.Entry(form_frame, font=("Arial", 16), width=25)
entry1.grid(row=1, column=1, padx=10, pady=10)

# Password Label and Entry
label2 = tk.Label(form_frame, text="Password:", font=("Arial", 16, "bold"), bg="#1f1c2c", fg="white")
label2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry2 = tk.Entry(form_frame, font=("Arial", 16), width=25, show="*")
entry2.grid(row=2, column=1, padx=10, pady=10)

# Buttons Frame within the form
button_frame = tk.Frame(form_frame, bg="#1f1c2c")
button_frame.grid(row=3, column=0, columnspan=2, pady=20)

# Login Button
login_button = tk.Button(
    button_frame, text="Login", font=("Arial", 16, "bold"),
    bg="green", fg="white", command=login, width=10
)
login_button.grid(row=0, column=0, padx=20)

# Exit Button
exit_button = tk.Button(
    button_frame, text="Exit", font=("Arial", 16, "bold"),
    bg="#f44336", fg="white", command=root.quit, width=10
)
exit_button.grid(row=0, column=2, padx=20)
registration_button = tk.Button(
    button_frame, text="Registration", font=("Arial", 16, "bold"),
    bg="#1976D2", fg="white", command=register, width=10
)
registration_button.grid(row=0, column=1, padx=20)

# Run the application
root.mainloop()