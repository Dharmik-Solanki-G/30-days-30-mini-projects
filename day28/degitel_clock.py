import tkinter as tk
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime("%A, %B %d, %Y \n %H:%M:%S")
    label_time.config(text=current_time)
    label_time.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.configure(bg="black")

# Create a label to display the time with Arial font
label_time = tk.Label(root, font=("Arial", 36), bg="black", fg="#04D9FF")
label_time.pack(pady=(20, 0))

# Run the update_time function to update the time display
update_time()

# Run the Tkinter event loop
root.mainloop()


