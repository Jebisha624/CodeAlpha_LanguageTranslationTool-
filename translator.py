from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator


# Function to translate text
def translate_text():
    try:
        source_lang = source_combo.get()
        target_lang = target_combo.get()

        text = input_text.get("1.0", END).strip()

        if not text:
            messagebox.showwarning("Warning", "Please enter some text!")
            return

        translated = GoogleTranslator(
            source=source_lang,
            target=target_lang
        ).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Function to copy translated text
def copy_text():
    translated = output_text.get("1.0", END).strip()

    if translated:
        root.clipboard_clear()
        root.clipboard_append(translated)
        messagebox.showinfo("Success", "Text copied successfully!")
    else:
        messagebox.showwarning("Warning", "Nothing to copy!")


# Main Window
root = Tk()
root.title("Language Translation Tool")
root.geometry("700x550")
root.resizable(False, False)

# Heading
heading = Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 18, "bold")
)
heading.pack(pady=10)

# Input Label
Label(
    root,
    text="Enter Text",
    font=("Arial", 12, "bold")
).pack()

# Input Text Box
input_text = Text(root, height=6, width=70)
input_text.pack(pady=5)

# Language Selection Frame
frame = Frame(root)
frame.pack(pady=10)

# Source Language
Label(
    frame,
    text="Source Language"
).grid(row=0, column=0, padx=10)

source_combo = ttk.Combobox(frame, width=15)
source_combo["values"] = (
    "en",  # English
    "ta",  # Tamil
    "hi",  # Hindi
    "fr",  # French
    "de",  # German
    "es"   # Spanish
)
source_combo.current(0)
source_combo.grid(row=0, column=1)

# Target Language
Label(
    frame,
    text="Target Language"
).grid(row=0, column=2, padx=10)

target_combo = ttk.Combobox(frame, width=15)
target_combo["values"] = (
    "ta",
    "en",
    "hi",
    "fr",
    "de",
    "es"
)
target_combo.current(0)
target_combo.grid(row=0, column=3)

# Translate Button
Button(
    root,
    text="Translate",
    command=translate_text,
    font=("Arial", 12, "bold"),
    width=15
).pack(pady=10)

# Output Label
Label(
    root,
    text="Translated Text",
    font=("Arial", 12, "bold")
).pack()

# Output Text Box
output_text = Text(root, height=6, width=70)
output_text.pack(pady=5)

# Copy Button
Button(
    root,
    text="Copy Text",
    command=copy_text,
    font=("Arial", 12, "bold"),
    width=15
).pack(pady=10)

# Run Application
root.mainloop()