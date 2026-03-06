import streamlit as st
from run_analysis import run_full_pipeline
import os
import shutil
# Page Config
st.set_page_config(page_title="ReelMind AI", layout="wide")

st.title("🎬 ReelMind AI: Viral Vibe Analyzer")
st.write("Enter a YouTube Reel URL to get a deep-dive story analysis.")

# Input
video_url = st.text_input("Paste Reel URL:", placeholder="https://www.youtube.com/shorts/...")

if st.button("Analyze"):
    if os.path.exists("data/temp/"):
        shutil.rmtree("data/temp/")
        os.makedirs("data/temp/")
    if not video_url:
        st.warning("Please enter a URL first!")
    else:
        # 1. Pipeline Execution with Status Container
        with st.status("Analyzing Video Content...", expanded=True) as status:
            st.write("Downloading video...")
            # Note: run_full_pipeline must now accept a progress_callback 
            # or handle internal progress. For now, we assume it's running.
            
            st.write("Processing visual timeline and OCR...")
            report = run_full_pipeline(video_url)
            
            status.update(label="Analysis Complete!", state="complete", expanded=False)

        # 2. Display the Storyboard
        st.subheader("Visual Storyboard")
        cols = st.columns(4) 
        # Display extracted frames (assuming 8 were saved to data/temp/)
        for i in range(1, 13):
            frame_path = f"data/temp/frame_{i}.jpg"
            if os.path.exists(frame_path):
                with cols[(i-1) % 4]:
                    st.image(frame_path, caption=f"Frame {i}", width="stretch")
        
        # 3. Display the Report
        st.markdown("---")
        st.header("The Vibe Report")
        st.write(report)