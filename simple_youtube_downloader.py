#%%
from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=Nf_c6xQY1ac&t=177s"

yt = YouTube(url, on_progress_callback=on_progress,use_oauth=True, allow_oauth_cache=True)
print(yt.title)

ys = yt.streams.get_highest_resolution()
ys.download()
# %%
