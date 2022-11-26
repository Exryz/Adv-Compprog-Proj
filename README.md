# YTDownloader v.2 prototype.

# YT v2 methods/function summary
YTDownloader is a GUI-based program for downloading Youtube Videos/Audio by using the Pytube library as the main functionality for the methods and tkinter for the UI.
<br>

## How to use
- With a command prompt open the code `python YTDownloader.py` or use your preferred IDE.
- Put the link of your video or audio in the text field.
- Select the format to download(Default resolution is set to 1080p and the youtube link can either be converted to an .mp3 file for audio or .mp4 file for video.)
- Finally press download button and the program will start to download the video.

## In this version
- We used Pytube instead of MoviePy because we counld't find a direct way to convert a youtube link to an .mp3 file.
- The downloaded file will be located in the program's current directory. 
- YTDownloader can download videos in 1080p or audio only.

## Required libraries/dependencies
- PyTube
- ffmpeg-python
- tkinter
- You can also install these with `pip install -r requirements.txt`
