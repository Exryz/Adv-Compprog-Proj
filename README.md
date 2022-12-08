# YTDownloader v.2 prototype.
<img src="https://media.discordapp.net/attachments/910816357917028392/1046031507749343262/image.png"/>
YTDownloader is a GUI-based program for downloading Youtube Videos/Audio by using the Pytube library as the main functionality for the methods and tkinter for the UI.
<br>

## How to use
- With a command prompt open the code `python YTDownloader.py` or use your preferred IDE.
- Put the link of your video or audio in the text field.
- Select the format to download(Default resolution is set to 1080p and the youtube link can either be converted to an .mp3 file for audio or .mp4 file for video.)
- Finally press download button and the program will start to download the video.

## In this version
- We used Pytube and Moviepy for format conversion mp4>mp3.
- The downloaded file will be located in the program's current directory. 
- YTDownloader can now download videos in 1080p or audio only.

## Required libraries/dependencies
- Python 3.10
- PyTube
- ffmpeg-python
- tkinter
- MoviePy
- You can also install these with `pip install -r requirements.txt`

## Video Presentation
[![Watch the video](https://cdn.discordapp.com/attachments/1044928036287549512/1050434223187709992/image.png)](https://youtu.be/oNzyH0M7cBg)
