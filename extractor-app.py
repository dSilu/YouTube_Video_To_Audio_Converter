# To install Tkinter: pip install tk-tools
# To install Pytube: pip install pytube

import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import os

# App window
window = tk.Tk()
window.geometry('600x300')
window.resizable(False, False)
window.title("YouTube Audio Extractor")

link = tk.StringVar()

# Extractor
def extractor():
    """
    Processes the input YouTube Link to mp3 file.
    """
    # Show processing message
    messagebox.showinfo(title='Extractor', message='Hold on\nProcessing...')
    
    # Extract the link
    v_link = YouTube(link.get())
    extracted = v_link.streams.filter(only_audio=True).first()
    # Save the extracted file to disk
    destination = "."
    output_file = extracted.download(output_path=destination)
    base, ext = os.path.splitext(output_file)
    new_file = base + '.mp3'
    os.rename(output_file, new_file)

    # Show success message
    messagebox.showinfo(title='Message', message=v_link.title +' has been extracted')


# Greetings
photo = tk.PhotoImage(file='download-icon-music.png')
img_label = tk.Label(window, image=photo).place(x=250, y=5)
url_label = tk.Label(window, text="Paste URL link below").place(x=245, y=150)

# URL input
link_input = tk.Entry(window, textvariable=link, width=40).place(x=145, y=190)

# Convert button
link_button = tk.Button(window, text='Convert', background='green', fg='white', command=extractor).place(x=280, y=230)

# Set window
window.mainloop()