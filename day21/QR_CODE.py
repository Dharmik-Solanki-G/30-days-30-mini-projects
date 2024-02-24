import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    url = url_entry.get()
    if url:
        qr_img = qrcode.make(url)
        qr_img = qr_img.resize((300, 300))  # Resize the QR code image
        qr_img_tk = ImageTk.PhotoImage(qr_img)
        qr_label.config(image=qr_img_tk)
        qr_label.image = qr_img_tk  # Keep a reference to avoid garbage collection
    else:
        messagebox.showerror("Error", "Please enter a URL")

# Create main window
root = tk.Tk()
root.title("QR Code Generator")
root.configure(bg='black')  # Set background color

# Set text color
tk.Label(root, text="Enter URL:", fg='white', bg='black').pack()

# Create URL input field
url_entry = tk.Entry(root, width=50, bg='white', fg='black')
url_entry.pack()

# Create generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr, bg='white', fg='black')
generate_button.pack()

# Create label to display QR code
qr_label = tk.Label(root, bg='black')
qr_label.pack()

# Run the main event loop
root.mainloop()
