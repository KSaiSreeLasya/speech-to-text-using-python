import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
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

# Header Frame
header_frame = tk.Frame(root, bg="#1f1c2c", height=150)
header_frame.place(x=0, y=0, relwidth=1)

# Load and resize the logo
original_logo = Image.open("hlogo.png")
resized_logo = original_logo.resize((130, 130), Image.Resampling.LANCZOS)
logo_image = ImageTk.PhotoImage(resized_logo)

# Place logo in the header frame
logo_label = tk.Label(header_frame, image=logo_image, bg="#1f1c2c")
logo_label.place(x=20, y=10)

# Header Label
header_label = tk.Label(
    header_frame,
    text=" Vocal Script",
    font=("Helvetica", 32, "bold"),
    bg="#1f1c2c",
    fg="#ffffff",
    pady=10
)
header_label.place(x=180, y=37)

# Caption Label
caption_label = tk.Label(
    header_frame,
    text="  Say It Once, Keep It Forever!",
    font=("Helvetica", 15, "italic"),
    fg="white",
    bg="#1f1c2c"
)
caption_label.place(x=188, y=93)

# Frame for the instructions
form_frame = tk.Frame(root, bg="#1f1c2c", padx=20, pady=20, relief="raised", borderwidth=3)
form_frame.place(relx=0.5, rely=0.6, anchor="center")  # Center the frame in the window

# Add the heading
heading_label = tk.Label(
    form_frame, text="Instructions:", font=("Arial", 18, "bold"), bg="#1f1c2c", fg="white"
)
heading_label.pack(anchor="w", pady=(0, 10))

# Add the instruction text
instructions = [
    "1. Registration: Create an account by entering your email, username, and password.",
    "2. Login: Log in using your registered username and password.",
    "3. Record: Record your script by clicking the 'Convert to Text' button.",
    "4. If the user's voice is inaudible or unclear due to surrounding disturbances, the system will automatically stop recording and turn off the microphone after 1 minute of inactivity.",
    "5. The system will continue recording as long as the user's voice is audible and the microphone remains active.",
    "6. Record: The microphone will turn off after 1-2 minutes; click the 'Convert to Text' button to stop, and you can continue recording by pressing the button again.",
    "7. Save: Save your recorded script into a Word document by clicking the 'Save Document' button.",
]

# Display instructions as labels
for instruction in instructions:
    instruction_label = tk.Label(
        form_frame, text=instruction, font=("Arial", 14), bg="#1f1c2c", fg="white", wraplength=1200, justify="left"
    )
    instruction_label.pack(anchor="w", pady=5)

# Run the Tkinter event loop
root.mainloop()
