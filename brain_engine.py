from groq import Groq
import os

import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def analyze_vibe(visuals, text, audio):
    prompt = f"""
    Analyze this meme/video content:
    - Visual description: {visuals}
    - Text overlay: {text}
    - Audio transcript: {audio}
    
    Why is this viral? Summarize the humor and context in 2 sentences.
    """
    
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )
    return response.choices[0].message.content

