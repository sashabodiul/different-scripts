from __future__ import unicode_literals
from pyfiglet import Figlet
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': True
}

preview = Figlet(font='slant')
print(preview.renderText('Youtube audio'))
url = input('Enter Youtube link for download:')
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([f'{url}'])