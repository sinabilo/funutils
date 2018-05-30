from __future__ import unicode_literals
import youtube_dl




url = "https://www.youtube.com/watch?v=FJfFZqTlWrQ"

    
def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    # 'format': 'bestaudio/best',       
    # 'outtmpl': '%(id)s',        
    'noplaylist' : True,        
    # 'progress_hooks': [my_hook],  
    'outtmpl' : "pk01-"
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    a = ydl.download([url])
    
import pathlib
rr = os.path.realpath("pk01-.mkv")
os.system("mplayer -novideo {}".format(rr))