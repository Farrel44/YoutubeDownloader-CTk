import customtkinter
from pytube import YouTube
from customtkinter import *
from tkinter import filedialog, StringVar

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")


def Widgets():
    headLabel = customtkinter.CTkLabel(app, text="Youtube Video Downloader using CustomTkinter",
                                       padx=15,
                                       pady=15,
                                       font=("Arial Bold", 20),
                                       wraplength=400)
    headLabel.pack(pady=10, padx=5)
    
    linkLabel = customtkinter.CTkLabel(app, text="Youtube Link :", pady=5, padx=5)
    linkLabel.pack(pady=5, padx=5)
    
    linkText = CTkEntry(app, textvariable=video_link, font=("Arial", 16))
    linkText.pack(pady=5, padx=5, fill="x", expand=True)
    
    destinationLabel = CTkLabel(app, text="File Destination : ", pady=5, padx=5)
    destinationLabel.pack(pady=5, padx=5)
    
    destinationEntry = customtkinter.CTkEntry(app, textvariable=download_Path, font=("Arial", 16))
    destinationEntry.pack(pady=5, padx=5, fill="x", expand=True)
    
    browseButton = customtkinter.CTkButton(app, text="Browse File", command=onBrowse)
    browseButton.pack(pady=5, padx=5)
    
    downloadButton = customtkinter.CTkButton(app, text="Download Video", command=onDownload, font=("Arial Bold", 16))
    downloadButton.pack(pady=20, padx=20)


def onBrowse():
    downloadDirectory = filedialog.askdirectory(initialdir="Change to your default folder destination", title="Save Video")
    download_Path.set(downloadDirectory)


def onDownload():
    YouTube_link = video_link.get()
    download_Folder = download_Path.get()
    
    try:
        getVideo = YouTube(YouTube_link)
        videoStream = getVideo.streams.get_highest_resolution()
        videoStream.download(download_Folder)
        show_messagebox("Download Successful", "Download completed successfully.")
    except Exception as e:
        show_messagebox("Error", f"An error occurred: {str(e)}")


def show_messagebox(title, message):
    dialog = customtkinter.CTkToplevel(app)
    dialog.title(title)
    dialog.geometry("300x150")
    messageLabel = customtkinter.CTkLabel(dialog, text=message)
    messageLabel.pack(padx=20, pady=20)
    
    okButton = customtkinter.CTkButton(dialog, text="Ok", command=dialog.destroy)
    okButton.pack(pady=10)


app = customtkinter.CTk()
app.title("Youtube Video Downloader")

video_link = StringVar()
download_Path = StringVar()

Widgets()

app.update_idletasks() 
app.resizable(False, False)

app.mainloop()
