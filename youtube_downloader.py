from pytube import Youtube

#Asking for the video link 

link = input("Please Enter the video link :")
#Youtube object 

yt = Youtube(link)
print("Title : ",yt.Title)
print("You want to download it ? (Y/N)")
confirmation = input()

if confirmation == "Y" or "y":
    stream = yt.streams.filter(progressive=True)
    print(stream)
    tag = int(input("\nEnter the itag of your preferred stream to download: "))
    video = yt.streams.get_by_itag(tag)
    print("\nDownloading ...")
    video.download()
    print("The Download is completed !")

else :
    print("bye")
    exit()