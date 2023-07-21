import asyncio

import pytube.exceptions
from pytube import YouTube, Playlist
import os, re
import moviepy.editor as mp


async def download_data(url, mode, path):
    if mode == 'Video':
        try:
            yt = YouTube(url)
            yt.streams.filter(only_audio=True).first.download(path)
        except pytube.exceptions.RegexMatchError:
            print('Exception')
    elif mode == 'Playlist':
        try:
            p = Playlist(url)
            for video in p.videos:
                video.streams.filter(only_audio=True).first().download(path)
        except:
            pass


async def convert_data(url, path):
    print(path)
    if url:
        for file in os.listdir(path):
            if re.search('mp4', file):
                mp4 = os.path.join(path, file)
                mp3 = os.path.join(path, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(mp4)
                new_file.write_audiofile(mp3, codec='libmp3lame')
                os.remove(mp4)


async def start_process(url, mode, path):
    task_download = asyncio.create_task(download_data(url, mode, path))
    await task_download
    task_convert = asyncio.create_task(convert_data(url, path))
    await task_convert
