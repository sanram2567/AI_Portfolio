import yt_dlp
import pandas as pd
import os

def download_reel(url, output_folder="data/reels"):
    os.makedirs(output_folder, exist_ok=True)
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
    return filename