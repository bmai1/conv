import tkinter as tk
from tkinter import messagebox

import yt_dlp
from pytube import YouTube

import os


class Convertor:
    def __init__(self, root):
        self.root = root

        root.title("Convertor")
        root.geometry("600x300")
        # root.configure(background='black')

        self.center_window(root)

        self.url_label = tk.Label(root, text="Enter YouTube URL:", font=("Helvetica Neue", 15))
        self.url_label.pack(pady=(75, 5))


        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=10)

        
        self.mp3_button = tk.Button(root, text="Download as MP3", font=("Helvetica Neue", 12), command=self.download_mp3)
        self.mp3_button.pack()

        self.mp4_button = tk.Button(root, text="Download as MP4", font=("Helvetica Neue", 12), command=self.download_mp4)
        self.mp4_button.pack()

        self.download_status_label = tk.Label(root, text="")
        self.download_status_label.pack()

    def center_window(self, window):

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Calculate the position of the window
        x = (screen_width - window.winfo_reqwidth()) // 2
        y = (screen_height - window.winfo_reqheight()) // 2

        x -= 200
        y -= 200
        # Set the position of the window
        window.geometry('+{}+{}'.format(x, y))

    def download_mp3(self):
        url = self.url_entry.get()
        url = self.remove_playlist_slug(url)

        if not url:
            messagebox.showerror("Error", "Please enter a valid YouTube URL.")
            return
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                # output path
                'outtmpl': os.path.join('output', '%(title)s.%(ext)s'),
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get('title', 'Title Unavailable')
                
            self.download_status_label.config(text=f"Download complete: {title}")

        except Exception as e:
            print(e)

    def download_mp4(self):
        url = self.url_entry.get()
        url = self.remove_playlist_slug(url)

        try:
            yt = YouTube(url)

            # stream = yt.streams.filter(file_extension='mp4').first()
            # stream.download("output_mov")

            yd = yt.streams.get_highest_resolution()
            yd.download("output_mov")

            self.download_status_label.config(text=f"Download complete: {yt.title}")
        except Exception as e:
            print(e)

    # download single video, not whole playlist
    def remove_playlist_slug(self, url):
        if '&list=' in url:
            url = url.split('&list=')[0]
        return url

root = tk.Tk()
app = Convertor(root)
root.mainloop()

# testing links
# https://www.youtube.com/watch?v=p3iDtps7dL8
# https://www.youtube.com/watch?v=IbKYcJ3DzYk&list=PLH1TkRvPd30Pa6QupChBNefWLREdW9Br9&index=9