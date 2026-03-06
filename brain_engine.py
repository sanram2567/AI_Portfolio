import os
from groq import Groq
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))



def analyze_vibe(visuals, text, audio):
    SYSTEM_PROMPT = """
    You are 'ReelMind', a Senior Social Media Intelligence Analyst. 
    Your goal is to deconstruct short-form video content to identify why it succeeds or fails.

    Analyze the provided data (Visual Sequence, OCR Text, and Subtitle Transcript) using this framework:

    1. **The Hook (0-3s):** Analyze the very first visual and the opening line of subtitles. Did it grab attention immediately?
    2. **Pacing & Rhythm:** Compare the speed of visual cuts (from Visual Sequence) with the tempo of the audio/subtitles. Is it frantic, slow-burn, or rhythmic?
    3. **Sentiment & Tone:** Using the subtitles and OCR, identify the emotional core (e.g., ironic, nostalgic, frantic, educational).
    4. **Cultural Context:** Identify any trending keywords or meme formats in the text.
    5. **The "Viral" Verdict:** Give a score from 1-10 on 'Potential Virality' and explain the 'X-factor' (the specific element that makes this video shareable).

    Keep your response professional, data-driven, and actionable.
    """

    user_input = f"""
    Analyze this video's vibe. 
    Visual sequence: {visuals}
    On-screen text: {text}
    Audio transcript: {audio}
    
    TASK: Do not treat the frames as separate images. Instead, tell me the STORY 
    progression from Start to End. Why do these elements make the video viral?
    """
    try:
        response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )
        return response.choices[0].message.content
    except Exception as e:
        return f"Brain Engine Error: {str(e)}"
        