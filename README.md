**ReelMind AI** 🚀
A Multimodal Content Intelligence Engine for Short-Form Video Analysis.

ReelMind AI is an automated pipeline designed to reverse-engineer viral content. By combining computer vision, OCR, and natural language processing, it extracts deep insights from video platforms (YouTube) to identify what makes content successful.

🏗️ **Technical Architecture**
ReelMind utilizes a modular pipeline to process video data:

**Ingestion**: Automated downloads via YouTube APIs.

**Vision Engine**: Keyframe extraction and visual analysis using state-of-the-art models (BLIP).

**Audio Engine**: Intelligent transcription engine that prioritizes official subtitles and falls back to OpenAI Whisper when necessary.

**OCR Engine**: Frame-level text extraction to capture on-screen messaging.

**Brain Engine**: A Llama 3.1-powered analytical core that synthesizes all inputs into a "Virality Score" and actionable strategy report.

🛠️ **Key Technologies**
Python | Streamlit | OpenAI Whisper | Llama 3.1

OpenCV (for frame processing)

YouTube Transcript API (for metadata-first transcription)

Git (Version Control)

📊 **Why This Project?**
ReelMind AI moves beyond simple transcription. It performs multimodal fusion—correlating visual pacing with audio sentiment to provide a 360-degree view of video performance. It demonstrates a production-ready approach to AI, featuring:

**Error-Handling**: Robust fallbacks for missing subtitles.

**Efficiency**: Caching strategies (st.cache_resource, st.cache_data) to optimize compute.

**Modularity**: Decoupled engines for easy scaling and testing.

🚀 **Getting Started**
Clone the repository: git clone https://github.com/sanram2567/ReelMind-AI.git

Install dependencies: pip install -r requirements.txt

Run the app: streamlit run streamlit_app.py
