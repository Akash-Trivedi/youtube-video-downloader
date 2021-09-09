# this is the first comment for git testing for modification.
# another edit for git.
from pytube import YouTube
import os
import math
PERCENTAGE_COMPLETION = 0


def on_progress(stream, chunk, bytes_remaining):
    global PERCENTAGE_COMPLETION
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = ((bytes_downloaded / total_size) * 100)
    percentage_of_completion= math.ceil(percentage_of_completion)

    # update the percentage_of_completion for new value
    if percentage_of_completion != PERCENTAGE_COMPLETION:
        PERCENTAGE_COMPLETION = percentage_of_completion
        print('=', end='')
        if percentage_of_completion == 100:
            print('>')


def download_audio(link):
    """
    This will extract mp3 from video and download it.
    :param link: str youtube video link
    :return: None
    """
    global PERCENTAGE_COMPLETION
    yt = YouTube(link, on_progress)
    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(output_path="mp3")

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    PERCENTAGE_COMPLETION = 0
    print(yt.title + " has been successfully downloaded.")


def download_video(link):
    """
    This will download video file of specific resolution
    :param link: str youtube video link
    :return: None
    """
    global PERCENTAGE_COMPLETION
    # todo: insert try except block for no internet, video NoneType object return.
    yt = YouTube(str(link))
    res1=0
    is_available= False
    while True:
        print("Select the video Quality for : "+ yt.title)
        res1 = int(input("1. 1080p\n2. 720p\n3. 480p\n4. 360p\n5. 240p\n6. 144p\n your choice: "))

        if res1 == 1:
            if type(yt.streams.filter(res='1080p').first()) is type(None):
                print('Resolution unavailable!')
                continue
            else:
                print(type(yt.streams.filter(res='1080p').first()))
                is_available=True
                res1= "1080p"
                break
        elif res1 == 2:
            if yt.streams.filter(res='720p').first() is type(None):
                print('Resolution unavailable!')
                continue
            else:
                is_available = True
                res1 = "720p"
                break
        elif res1 == 3:
            if yt.streams.filter(res='480p').first() is type(None):
                continue
            else:
                is_available = True
                res1 = "480p"
                break
        elif res1 == 4:
            if yt.streams.filter(res='360p').first() is type(None):
                print('Resolution unavailable!')
                continue
            else:
                is_available = True
                res1 = "360p"
                break
        elif res1 == 5:
            if type(yt.streams.filter(res='2400p').first()) is type(None):
                print('Resolution unavailable!')
                continue
            else:
                is_available = True
                res1 = "240p"
                break
        elif res1==6:
            is_available= True
            res1= "144p"
            break


    if(is_available):
        print('Video Available in '+res1)
        print('Downloading File...')
        video = yt.streams.filter(res=res1).first()
        out_file = video.download(output_path='mp4')
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp4'
        os.rename(out_file, new_file)
        PERCENTAGE_COMPLETION = 0
        print(yt.title + " has been successfully downloaded.")
