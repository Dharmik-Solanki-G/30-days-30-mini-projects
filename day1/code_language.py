import tkinter as tk
from tkinter import messagebox
import random

def encode(word):
    if len(word) >= 3:
        first_letter = word[0]
        word = word[1:] + first_letter
        random_chars = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3))
        encoded_word =  random_chars + word + random_chars
    else:
        encoded_word = word[::-1]
    return encoded_word

def decode(word):
    if len(word) < 3:
        decoded_word = word[::-1]
    else:
        last_letter = word[-3:]
        first_letters = word[:4]
        first_letter=word[-4]
        remaining_letter=word[3:-4]
        decoded_word = first_letter + remaining_letter
           # Adjusted this line
    return decoded_word


def process_input():
    choice = choice_var.get()
    message = input_entry.get()

    if choice == 'code':
        result = [encode(word) for word in message.split(" ")]
        result_text.set(" ".join(result))
    elif choice == 'decode':
        result = [decode(word) for word in message.split(" ")]
        result_text.set(" ".join(result))
    else:
        messagebox.showinfo("Error", "Invalid choice. Please enter 'code' or 'decode'.")

# Create main window
window = tk.Tk()
window.title("Message Coder And Decoder")

# Create widgets
choice_var = tk.StringVar()
choice_var.set("code")
input_label = tk.Label(window, text="Enter the message:")
input_entry = tk.Entry(window, width=100)
result_label = tk.Label(window, text="Result:")
result_text = tk.StringVar()
result_entry = tk.Entry(window, width=100, textvariable=result_text, state="readonly")
code_button = tk.Button(window, text="Code/Decode", command=process_input, bg='black',fg='white')

# Arrange widgets using the grid layout
input_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
input_entry.grid(row=0, column=1, padx=10, pady=10)
result_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
result_entry.grid(row=1, column=1, padx=10, pady=10)
code_button.grid(row=2, column=0, columnspan=2, pady=10)
tk.Radiobutton(window, text="Code", variable=choice_var, value="code").grid(row=3, column=0)
tk.Radiobutton(window, text="Decode", variable=choice_var, value="decode").grid(row=3, column=1)

# Start the GUI event loop
window.mainloop()
