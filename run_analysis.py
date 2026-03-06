from vision_engine import generate_caption
from ocr_engine import extract_text
from audio_engine import transcribe_audio
from brain_engine import analyze_vibe

def run_full_pipeline(video_path, frame_path):
    print("--- 1. Extracting Visuals ---")
    visual = generate_caption(frame_path)
    
    print("--- 2. Extracting Text ---")
    text = extract_text(frame_path)
    
    print("--- 3. Extracting Audio ---")
    audio = transcribe_audio(video_path)
    
    print("--- 4. Synthesizing 'Vibe Report' ---")
    report = analyze_vibe(visual, text, audio)
    
    print("\n--- FINAL AI VIBE REPORT ---")
    print(report)

if __name__ == "__main__":
    run_full_pipeline("data/reels/BANANA (Animation Meme).mp4", "data/frames/BANANA (Animation Meme)/frame_19.jpg")