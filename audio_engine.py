import whisper
import os

# Load the model
# 'base' is good for testing; 'small' or 'medium' for production accuracy
model = whisper.load_model("base")

def transcribe_audio(video_path):
    print(f"Transcribing: {video_path}...")
    # This automatically extracts audio and transcribes it
    result = model.transcribe(video_path)
    return result["text"]

if __name__ == "__main__":
    # Point this to one of your downloaded videos
    video_file = "data/reels/BANANA (Animation Meme).mp4" 
    if os.path.exists(video_file):
        transcript = transcribe_audio(video_file)
        print("\n--- TRANSCRIPT ---")
        print(transcript)
    else:
        print("Please provide a valid path to an MP4 file in your data folder.")