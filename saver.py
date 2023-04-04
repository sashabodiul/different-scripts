from pytube import YouTube
from pyfiglet import Figlet
import time
import os


# url input from user
with open('audiolinks.txt', 'r') as f:
    urls = f.readlines()
counter = 0

for link in urls:
    if counter == 0:
        preview = Figlet(font='slant')
        print(f"{preview.renderText('Wait for loading')}",end='\r')
        time.sleep(1)
    yt = YouTube(link)
    
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    counter += 1
    # check for destination to save file
    print(f"                Saved {counter} files",end="\r")
    destination = 'music'
    
    # download the file
    out_file = video.download(output_path=destination)
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

preview = Figlet(font='slant')
print(preview.renderText(f'{counter} FILES SAVED'))
