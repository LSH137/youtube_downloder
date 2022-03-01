from pytube import YouTube
from pytube import Playlist

downlodaFolder = input("enter the path for download: ")
url = input("enter youtube url: ")

playlist = Playlist(url)

for video in playlist:
    print(video)
    yt = YouTube(video)
    video_select = yt.streams.get_by_itag(22)
    video_select.download(downlodaFolder, yt.title + '.mp4')