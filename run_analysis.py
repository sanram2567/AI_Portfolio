import re
from ingest import download_reel
from vision_engine import extract_multiple_frames
from ocr_engine import extract_text
from audio_engine import get_audio_transcript  # Updated Import
from brain_engine import analyze_vibe

def extract_video_id(url):
    """Utility to extract ID from various YouTube URL formats."""
    video_id_match = re.search(r'(?:v=|/)([0-9A-Za-z_-]{11}).*', url)
    return video_id_match.group(1) if video_id_match else None

def run_full_pipeline(url):
    print("--- 1. Ingesting Video ---")
    video_path = download_reel(url)
    video_id = extract_video_id(url) # Extract ID for subtitle engine
    
    print("--- 2. Extracting Multi-Frame Visuals ---")
    visual_sequence = extract_multiple_frames(video_path, num_frames=12)
    
    print("--- 3. Extracting Text & Audio ---")
    ocr_results = []
    for i in range(1, 9): 
        text = extract_text(f"data/temp/frame_{i}.jpg")
        if text.strip():
            ocr_results.append(f"Frame {i} text: {text}")
    
    full_ocr_text = "\n".join(ocr_results)
    
    # Now passing both ID and Path to the smart audio engine
    audio = get_audio_transcript(video_id, video_path) 
    
    print("--- 4. Synthesizing Vibe Report ---")
    report = analyze_vibe(visual_sequence, full_ocr_text, audio)
    
    return report

if __name__ == "__main__":
    # Example usage
    run_full_pipeline("https://www.youtube.com/watch?v=exampleID123")