import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import os

def download_video():
    try:
        if not os.path.exists("downloader"):
            os.makedirs("downloader")

        yt = YouTube(url_entry.get())

        stream = yt.streams.get_highest_resolution()

        stream.download(output_path="downloader/")

        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("YouTube Video Downloader")

root.configure(bg="lightblue")
root.attributes('-topmost', 1)

url_label = tk.Label(root, text="Enter YouTube URL:", bg="lightblue", font=("Arial Bold", 12, "underline"))
url_label.pack()

url_entry = tk.Entry(root, width=50, font=("Arial Bold", 12))
url_entry.pack()

download_button = tk.Button(root, text="Download Video", command=download_video, font=("Arial Bold", 12))
download_button.pack()

root.mainloop()
