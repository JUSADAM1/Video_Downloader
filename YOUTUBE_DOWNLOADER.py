# One can do alot with future like I can take pasted old imports and roll them back to where they work in python 3
# Mean stuff that dont work in python 3 but did work in python 2
# well if I used Bulletin I canold stuff with the new stuff.
from __future__ import unicode_literals

# Youtube video downloader
import youtube_dl

# Dictionary
ydl_opts = {}
# User input
Userinput = input('Please Enter YouTube URL HERE: ')
# calls the library ->Force redirects Url to unicode into python
# Technically meaning I had to make the python 2 code because the library hasnt been updated for a while
# So I converted the code to python 2 ---> 3
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    # Pulls the youtube video.
    ydl.download([Userinput])

# Ok I just found a way to copy and download YouTube Videos. So I have a question so is that technically copyright.
# Because I have downloaded a whole bunch of music videos and stuff. On top off Chatquisha does it also so is that bad.
