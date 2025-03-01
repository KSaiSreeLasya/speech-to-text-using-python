import tkinter as tk
import speech_recognition as sr
from tkinter import messagebox
from docx import Document
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageTk
import subprocess
import sys


def Speech_to_Text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            txtSpeech.insert(tk.END, text + "\n")
        except sr.UnknownValueError:
            txtSpeech.insert(tk.END, "Could not understand audio\n")
        except sr.RequestError as e:
            txtSpeech.insert(tk.END, f"Error: {e}\n")


def instruction():
    root.destroy()
    subprocess.Popen([sys.executable, "instructions.py"])


def save_as_word():
    text = txtSpeech.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Save", "No text available to save.")
        return
    file = asksaveasfilename(defaultextension=".docx", filetypes=[("Word Documents", "*.docx")])
    if file:
        doc = Document()
        doc.add_paragraph(text)
        doc.save(file)
        messagebox.showinfo("Save", "Text saved as Word document successfully!")


def reset_txtSpeech():
    txtSpeech.delete("1.0", tk.END)


def exit_system():
    result = messagebox.askquestion("Exit System", "Confirm if you want to exit?")
    if result == 'yes':
        messagebox.showinfo("Exit", "Goodbye!")
        root.destroy()


# Create the main application window
root = tk.Tk()
root.title("Speech to Text Application")
root.geometry("1200x700")
root.configure(bg="#f5f5f5")

# Header Frame
header_frame = tk.Frame(root, bg="#1f1c2c", height=100)
header_frame.pack(fill=tk.X)

original_logo = Image.open("hlogo.png")
resized_logo = original_logo.resize((100, 100), Image.Resampling.LANCZOS)
logo_image = ImageTk.PhotoImage(resized_logo)

# Place logo in the header frame
logo_label = tk.Label(header_frame, image=logo_image, bg="#2c2738")
logo_label.place(x=20, y=6)

header_label = tk.Label(
    header_frame,
    text="Vocal Script",
    font=("Helvetica", 25, "bold"),
    bg="#1f1c2c",
    fg="#ffffff",
    pady=10,
)
header_label.place(x=180, y=8)

caption_label = tk.Label(
    header_frame,
    text=" Say It Once, Keep It Forever!",
    font=("Helvetica", 16, "italic"),
    fg="white",
    bg="#1f1c2c",
    pady=10
)
caption_label.place(x=180, y=52)

# Main Frame
main_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, relief="ridge", bd=5)
main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

# Create a frame for the title and instruction button
title_frame = tk.Frame(main_frame, bg="#ffffff")
title_frame.pack(fill=tk.X, pady=10)
title_frame.columnconfigure(0, weight=1)  # Allow the heading to stretch
title_frame.columnconfigure(1, weight=0) 
# Add the "Instructions" button in the title frame, aligned to the left
btnInstructionTop = tk.Button(
    title_frame,
    text="Instructions",
    bg="#8E44AD",
    fg="#ffffff",
    activebackground="#732D91",
    activeforeground="#ffffff",
    font=("Helvetica", 14, "bold"),
    relief="raised",
    bd=3,
    command=instruction,
    width=15,
)
btnInstructionTop.place(x=1230,y=10) # Left aligned button

# Add the "Speech to Text" heading in the title frame
lblTitle = tk.Label(
    title_frame,
    font=("Helvetica", 28, "bold"),
    bg="#ffffff",
    fg="#333333",
    text="Speech to Text",
)
lblTitle.grid(row=0, column=1, padx=10, sticky="w")  # Centered heading

# Ensure the title expands in the remaining space
title_frame.columnconfigure(1, weight=1)

# Add the text box below the title frame
txtSpeech = tk.Text(
    main_frame,
    font=("Arial", 16),
    bg="#f0f0f0",
    fg="#000000",
    width=120,
    height=15,
    relief="sunken",
    bd=5,
)
txtSpeech.pack(pady=20)

# Button Frame
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(fill=tk.X, pady=10)

button_style = {
    "font": ("Helvetica", 14, "bold"),
    "width": 28,
    "height": 2,
    "relief": "raised",
    "bd": 3,
}

btnConvert = tk.Button(
    button_frame,
    text="Convert to Text",
    bg="#4CAF50",
    fg="#ffffff",
    activebackground="#45a049",
    activeforeground="#ffffff",
    command=Speech_to_Text,
    **button_style,
)
btnConvert.pack(side=tk.LEFT, padx=20)

btnSave = tk.Button(
    button_frame,
    text="Save Document",
    bg="#2196F3",
    fg="#ffffff",
    activebackground="#1976D2",
    activeforeground="#ffffff",
    command=save_as_word,
    **button_style,
)
btnSave.pack(side=tk.LEFT, padx=20)

btnReset = tk.Button(
    button_frame,
    text="Reset",
    bg="#FFC107",
    fg="#ffffff",
    activebackground="#FFA000",
    activeforeground="#ffffff",
    command=reset_txtSpeech,
    **button_style,
)
btnReset.pack(side=tk.LEFT, padx=20)

btnExit = tk.Button(
    button_frame,
    text="Exit",
    bg="#f44336",
    fg="#ffffff",
    activebackground="#D32F2F",
    activeforeground="#ffffff",
    command=exit_system,
    **button_style,
)
btnExit.pack(side=tk.LEFT, padx=20)

# Run the application
root.mainloop()
