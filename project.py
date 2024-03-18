
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from pytube import YouTube

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x350")
root.configure(bg="#86B6F6")

# Create input fields for URL and resolution
url_label = ttk.Label(root, text="Enter YouTube video URL:")
url_label.pack()
url_entry = ttk.Entry(root, width=40)
url_entry.pack()
url_label.pack(pady=10)


resolution_label = ttk.Label(root, text="Select resolution:")
resolution_label.pack()
resolution_var = tk.StringVar()
resolution_combobox = ttk.Combobox(root, textvariable=resolution_var)
resolution_combobox.pack()
resolution_label.pack(pady=10)

# Function to download video when the button is clicked
def download_video():
    url = url_entry.get()
    resolution = resolution_var.get()

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, res=resolution).first()
        if not stream:
            stream = yt.streams.get_highest_resolution()
        stream.download()
        tk.messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error downloading video: {e}")

# Create download button
download_button = ttk.Button(root, text="Download", command=download_video)
download_button.pack()

# Run the GUI
root.mainloop()
