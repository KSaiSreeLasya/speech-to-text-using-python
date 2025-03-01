import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
from tkinter import Label, Frame, Canvas
from PIL import Image, ImageTk

def open_main_app():
    root.destroy()
    subprocess.Popen([sys.executable, "login.py"])

def exit_home():
    result = messagebox.askquestion("Exit Home Page", "Are you sure you want to exit?")
    if result == 'yes':
        messagebox.showinfo("Exit", "Goodbye!")
        root.destroy()

# Create the main window
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

# Buttons Frame
button_frame = Frame(root, bg="#1f1c2c")
button_frame.place(relx=0.5, rely=0.8, anchor="center")

# Button Style
button_style = {
    "font": ('Helvetica', 14, 'bold'),
    "width": 20,
    "height": 2,
    "relief": "groove",
    "bd": 3
}

# Start Application Button
start_button = tk.Button(button_frame, text="Start Application", bg="#4CAF50", fg="#ffffff",
                         activebackground="#45a049", activeforeground="#ffffff",
                         **button_style, command=open_main_app)
start_button.grid(row=0, column=0, padx=20, pady=10)

# Exit Button
exit_button = tk.Button(button_frame, text="Exit", bg="#f44336", fg="#ffffff",
                        activebackground="#e53935", activeforeground="#ffffff",
                        **button_style, command=exit_home)
exit_button.grid(row=0, column=1, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
