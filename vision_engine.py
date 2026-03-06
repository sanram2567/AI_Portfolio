import cv2
import os

def extract_frames(video_path, frames_per_second=2):
    # Create a folder for frames
    video_name = os.path.basename(video_path).split('.')[0]
    output_folder = f"data/frames/{video_name}"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    vidcap = cv2.VideoCapture(video_path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    hop_interval = int(fps / frames_per_second) # How many frames to skip
    
    count = 0
    saved_count = 0
    success, image = vidcap.read()

    print(f"Analyzing video: {video_name}")
    
    while success:
        # Only save frames at our interval (e.g., 1 frame per second)
        if count % hop_interval == 0:
            frame_filename = f"{output_folder}/frame_{saved_count}.jpg"
            cv2.imwrite(frame_filename, image)
            saved_count += 1
        
        success, image = vidcap.read()
        count += 1

    vidcap.release()
    print(f"Done! Saved {saved_count} frames to {output_folder}")

# --- TEST IT ---
video_file = "C:/Users/Sanjana Raman/AI_Portfolio/data/reels/BANANA (Animation Meme).mp4"
if os.path.exists(video_file):
   extract_frames(video_file)