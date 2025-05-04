import os
import tkinter as tk
from tkinter import messagebox
import yt_dlp


def download_video():
    url = url_entry.get()
    download_type = download_type_var.get().lower()
    
    if not url:
        messagebox.showerror("Error", "Please provide a valid URL.")
        return

    ffmpeg_path = "C:/ffmpeg/bin"
    
    if not os.path.exists(os.path.join(ffmpeg_path, "ffmpeg.exe")):
        messagebox.showerror("Error", "FFmpeg not found at the specified location!")
        return

    ydl_opts = {
        'ffmpeg_location': ffmpeg_path,
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
    }

    if download_type == 'mp3':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Download completed!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")



window = tk.Tk()
window.title("YouTube Downloader")


url_label = tk.Label(window, text="Video URL:")
url_label.pack(padx=10, pady=5)

url_entry = tk.Entry(window, width=40)
url_entry.pack(padx=10, pady=5)

download_type_var = tk.StringVar(value="mp4")  # Default to mp4

mp4_radio = tk.Radiobutton(window, text="MP4 (Video)", variable=download_type_var, value="mp4")
mp4_radio.pack(padx=10, pady=5)

mp3_radio = tk.Radiobutton(window, text="MP3 (Audio)", variable=download_type_var, value="mp3")
mp3_radio.pack(padx=10, pady=5)

# Download button
download_button = tk.Button(window, text="Download", command=download_video)
download_button.pack(padx=10, pady=20)

# Start the GUI loop
window.mainloop()
