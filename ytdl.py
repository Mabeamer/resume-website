from pytube import YouTube

import sys
#https://pytube.io/en/latest/user/quickstart.html#downloading-a-video
#https://www.youtube.com/watch?v=8u-_Uh89R9w

def converter(userLink):
    print('init')
    ytLink = YouTube(userLink)
    print(ytLink.streams.filter(file_extension='mp4'))

    #ytLink.streams.filter(res='360p').first.download()
    dl = ytLink.streams.get_by_itag(18)
    dl.download()
 
