import tkinter as tk
from tkinter import messagebox
import datetime
import time
import winsound

def set_alarm():
    alarm_time = entry.get()
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        while True:
            current_time = datetime.datetime.now()
            if current_time.hour == alarm_hour and current_time.minute == alarm_minute:
                messagebox.showinfo("Alarm", "Wake up!")
                # Play sound for 10 seconds
                winsound.Beep(1000, 10000)
                break
            time.sleep(1)
    except ValueError:
        messagebox.showerror("Error", "Invalid time format! Please enter time in HH:MM format.")

# Create main window
root = tk.Tk()
root.title("Alarm Clock")

# Create label
label = tk.Label(root, text="Enter alarm time (HH:MM):")
label.pack()

# Create entry
entry = tk.Entry(root)
entry.pack()

# Create set alarm button
button = tk.Button(root, text="Set Alarm", command=set_alarm)
button.pack()

# Run the main event loop
root.mainloop()
