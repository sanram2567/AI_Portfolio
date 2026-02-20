import yt_dlp
import pandas as pd
import os

def download_video(url, category="reels"):
    # Ensure folders exist
    save_path = f"data/{category}/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Settings for the downloader
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{save_path}%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Extract info without downloading first to log it
        info = ydl.extract_info(url, download=True)
        
        # Create a simple log entry (Roadmap: Data Manipulation)
        video_data = {
            "title": info.get('title'),
            "duration": info.get('duration'),
            "category": category,
            "filename": f"{info.get('title')}.{info.get('ext')}"
        }
        return video_data

# --- TEST IT ---
link = "https://youtube.com/shorts/Ce1DVzpUTFg?si=BkvgIjlJ8tZkxflg"
data = download_video(link)
print(f"Successfully downloaded: {data['title']}")