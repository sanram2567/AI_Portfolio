from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import csv
import os

# Load a dedicated Captioning model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image_path):
    image = Image.open(image_path).convert('RGB')
    
    # Let the model generate the text itself!
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    
    return processor.decode(out[0], skip_special_tokens=True)

def log_analysis(filename, caption):
    file_exists = os.path.isfile('analysis_log.csv')
    with open('analysis_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Frame Name', 'AI Caption'])
        writer.writerow([filename, caption])

# Test it
frame_folder = "data/frames/BANANA (Animation Meme)"
for filename in os.listdir(frame_folder):
    if filename.endswith(".jpg"):
        path = os.path.join(frame_folder, filename)
        caption = generate_caption(path)
        log_analysis(filename, caption)
        print(f"Logged: {filename} -> {caption}")