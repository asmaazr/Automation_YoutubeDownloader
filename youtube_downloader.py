from pytube import YouTube
import os
import sys

#customizing the command 
link = str(sys.argv[1])

def download():
    yt = YouTube(link)
    stream = yt.streams.filter(progressive=True)
    video = yt.streams.get_highest_resolution()
    print("\nDownloading ...")
    vd = video.download()
    print("The Download is completed !")

if __name__ == "__main__":
    download()

