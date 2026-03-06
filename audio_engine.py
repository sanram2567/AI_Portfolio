import whisper
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

# We use cache_data here since the output is a string (text)
@st.cache_data
def get_audio_transcript(video_id, video_path):
    """
    Fetches official subtitles if available, otherwise falls back to Whisper.
    video_id: The ID from the YouTube URL (e.g., 'dQw4w9WgXcQ')
    video_path: The local path to the downloaded MP4 file
    """
    # 1. ATTEMPT: Fetch official subtitles
    try:
        print("Attempting to fetch official subtitles...")
        yt = YouTubeTranscriptApi()
        transcript_list = yt.list(video_id)
        # Attempt to find English, will auto-select manually created then generated
        transcript = transcript_list.find_transcript(['en'])
        data = transcript.fetch()
        
        # Combine into a single text block
        return " ".join([entry.text for entry in data])
        
    except (TranscriptsDisabled, NoTranscriptFound):
        print("No official subtitles found, falling back to Whisper...")
        
        # 2. FALLBACK: Use Whisper (heavy processing)
        # Ensure 'base' model is loaded efficiently or cached
        model = whisper.load_model("base")
        result = model.transcribe(video_path)
        return result["text"]