from requests import get
from re import findall
from handler import download_audio, download_video

input_link= input('Enter video/playlist link(YouTube): ')

#common links holder
video_links= []

print("1. Download mp3: ")
print("2. Download mp4: ")
choice = int(input("Your Choice: "))


# get link details
#removing redundancy
if len(findall('/playlist\?', input_link)):
    playlist_data = get(input_link).content
    playlist_data = str(playlist_data)
    video_links = list(set(findall(r'videoId\":\"[\S]{11}\"', playlist_data)))

    for i in range(len(video_links)):
        video_links[i] = "https://www.youtube.com/watch?v=" + video_links[i][10:]
else:
    video_links.insert(0, input_link)


if choice==1:
    for i in range(len(video_links)):
        download_audio(video_links[i])

elif choice == 2:
    for i in range(len(video_links)):
        download_video(video_links[i])
