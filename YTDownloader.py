# Importing the packages
import os
import moviepy.editor as mp
from tkinter import *
from tkinter import messagebox
from pytube import YouTube
#Our YTDownloader program is a GUI for downloading Youtube videos, using the Pytube library as the main functionality and tkinter for the UI.
#was previously using moviepy but it didn't support the conversion from mp4 to mp3.
#The downloaded video/audio will be saved in the current directory at the moment. 


class YTDownloader(Tk):

    # For the window constructor
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # Configuring the window and grid (final desing)
        # self.geometry("651x424")
        # ui size

        self.geometry("500x150")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.title(r"Youtube Downloader")
        self.iconbitmap("yticon.ico")
        self.resizable(False, False)
        self.createWidgets()

    # Functionality
    def downloadLink(self, option):
        try:
            yt = YouTube(self.link.get())
        except Exception:
            return messagebox.showerror(
                "Syntax error",
                "The link is not supported or was misspelled"
                )

        file = yt.streams.filter(res="1080p").first() #Selected video resolution to download

        if (file is None):
            file = yt.streams.first()


        out_file = file.download()
        base, ext = os.path.splitext(out_file)

        if (option == 0):
            new_file = mp.VideoFileClip(out_file)
            new_file.audio.write_audiofile(base + '.mp3')
            new_file.close()
            os.remove(out_file)

        if (option == 1):
            new_file = base + '.mp4'
            os.rename(out_file, new_file)

        self.link.delete(0, 'end')

        messagebox.showinfo(
            "Success", 
            "The" + yt.title + " has been successfully downloaded")

    # GUI Creation
    def createWidgets(self):
        option_download = IntVar()

        self.title = Label(self, font=12, text="Youtube Video downloader")
        self.title.grid(row=0, column=0, columnspan=2, padx=1, ipady=6)

        self.link = Entry(self)
        self.link.grid(row=1, column=0, columnspan=2, rowspan=2, padx=10, pady=5, sticky=W+E)

        self.audio = Radiobutton(self, text="Audio", variable=option_download, value=0)
        self.audio.grid(row=3, column=0)

        self.video = Radiobutton(self, text="Video", variable=option_download, value=1)
        self.video.grid(row=3, column=1)

        self.download = Button(self, height=2, text="Download", command=lambda: self.downloadLink(option_download.get()))
        self.download.grid(row=4, column=0, columnspan=2, rowspan=6, padx=10, pady=5, sticky=S+N+E+W)


root = YTDownloader()
root.mainloop()
