import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk

# Map error correction options to corresponding values
ERROR_CORRECTION_MAP = {
    "L": qrcode.constants.ERROR_CORRECT_L,
    "M": qrcode.constants.ERROR_CORRECT_M,
    "Q": qrcode.constants.ERROR_CORRECT_Q,
    "H": qrcode.constants.ERROR_CORRECT_H
}

def generate_qr():
    url = url_entry.get()
    if url:
        qr = qrcode.QRCode(
            version=version_var.get(),
            error_correction=ERROR_CORRECTION_MAP[error_correction_var.get()],
            box_size=box_size_var.get(),
            border=border_var.get()
        )
        qr.add_data(url)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color=fill_color_entry.get(), back_color=back_color_entry.get())
        qr_img.save('generated_qr.png')
        
        # Display QR code image in GUI
        qr_img = qr_img.resize((200, 200))  # Resize the QR code image
        qr_img_tk = ImageTk.PhotoImage(qr_img)
        qr_label.config(image=qr_img_tk)
        qr_label.image = qr_img_tk  # Keep a reference to avoid garbage collection
        
        messagebox.showinfo("Success", "QR Code generated successfully!")
    else:
        messagebox.showerror("Error", "Please enter a URL")

def browse_save_location():
    save_location = filedialog.askdirectory()
    if save_location:
        save_location_entry.delete(0, tk.END)
        save_location_entry.insert(0, save_location)

# Create main window
root = tk.Tk()
root.title("QR Code Generator")

# URL input field
url_label = tk.Label(root, text="Enter URL:")
url_label.grid(row=0, column=0, padx=10, pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=5)

# QR options
options_frame = tk.LabelFrame(root, text="QR Options")
options_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky="ew")

version_var = tk.IntVar()
version_var.set(1)
version_label = tk.Label(options_frame, text="Version:")
version_label.grid(row=0, column=0, padx=5, pady=5)
version_entry = tk.Entry(options_frame, textvariable=version_var)
version_entry.grid(row=0, column=1, padx=5, pady=5)

error_correction_var = tk.StringVar()
error_correction_var.set('H')
error_correction_label = tk.Label(options_frame, text="Error Correction:")
error_correction_label.grid(row=0, column=2, padx=5, pady=5)
error_correction_entry = tk.Entry(options_frame, textvariable=error_correction_var)
error_correction_entry.grid(row=0, column=3, padx=5, pady=5)

box_size_var = tk.IntVar()
box_size_var.set(10)
box_size_label = tk.Label(options_frame, text="Box Size:")
box_size_label.grid(row=1, column=0, padx=5, pady=5)
box_size_entry = tk.Entry(options_frame, textvariable=box_size_var)
box_size_entry.grid(row=1, column=1, padx=5, pady=5)

border_var = tk.IntVar()
border_var.set(4)
border_label = tk.Label(options_frame, text="Border:")
border_label.grid(row=1, column=2, padx=5, pady=5)
border_entry = tk.Entry(options_frame, textvariable=border_var)
border_entry.grid(row=1, column=3, padx=5, pady=5)

fill_color_label = tk.Label(options_frame, text="Fill Color:")
fill_color_label.grid(row=2, column=0, padx=5, pady=5)
fill_color_entry = tk.Entry(options_frame)
fill_color_entry.grid(row=2, column=1, padx=5, pady=5)

back_color_label = tk.Label(options_frame, text="Background Color:")
back_color_label.grid(row=2, column=2, padx=5, pady=5)
back_color_entry = tk.Entry(options_frame)
back_color_entry.grid(row=2, column=3, padx=5, pady=5)

# Save location
save_location_label = tk.Label(root, text="Save Location:")
save_location_label.grid(row=2, column=0, padx=10, pady=5)
save_location_entry = tk.Entry(root, width=50)
save_location_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_save_location)
browse_button.grid(row=2, column=4, padx=5, pady=5)

# QR code display
qr_label = tk.Label(root)
qr_label.grid(row=3, column=0, columnspan=4, pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.grid(row=4, column=0, columnspan=4, pady=10)

# Run the main event loop
root.mainloop()
