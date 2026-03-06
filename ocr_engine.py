import easyocr

# Initialize the reader (English language)
reader = easyocr.Reader(['en'], gpu=False) # Set gpu=True if you have CUDA

def extract_text(image_path):
    # Perform text detection and recognition
    results = reader.readtext(image_path, detail=0)
    # Join the detected text snippets into one string
    return " ".join(results)

# Test run
if __name__ == "__main__":
    text = extract_text("data/frames/BANANA (Animation Meme)/frame_0.jpg")
    print(f"Detected Text: {text}")