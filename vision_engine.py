import cv2
import os
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import streamlit as st

# 1. DEFINE THE LOADER FIRST
@st.cache_resource
def load_vision_model():
    print("Loading BLIP model into RAM...")
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model



def extract_multiple_frames(video_path, num_frames=8):
    temp_dir = "data/temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Load model once
    processor, model = load_vision_model()
    
    # Create the progress UI in the sidebar or main area
    progress_bar = st.progress(0, text="Initializing Vision Engine...")
    
    captions = []
    for i in range(1, num_frames + 1):
        # Update Progress Bar (0.0 to 1.0)
        progress_val = i / num_frames
        progress_bar.progress(progress_val, text=f"Analyzing Frame {i} of {num_frames}...")
        
        pos = int(total_frames * (i / (num_frames + 1)))
        timestamp = round(pos / fps, 2)
        cap.set(cv2.CAP_PROP_POS_FRAMES, pos)
        
        ret, frame = cap.read()
        if ret:
            temp_path = os.path.join(temp_dir, f"frame_{i}.jpg")
            cv2.imwrite(temp_path, frame)
            
            # Captioning logic
            image = Image.open(temp_path).convert('RGB')
            inputs = processor(images=image, return_tensors="pt")
            out = model.generate(**inputs, max_new_tokens=25)
            desc = processor.decode(out[0], skip_special_tokens=True)
            captions.append(f"[{timestamp}s]: {desc}")
            
    cap.release()
    progress_bar.empty() # Remove bar when done
    return "\n".join(captions)
