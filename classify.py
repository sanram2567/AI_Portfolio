from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import csv
import os
from ocr_engine import extract_text

# Load a dedicated Captioning model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image_path):
    # Load and prepare the image
    image = Image.open(image_path).convert('RGB')
    
    # 1. Use the processor to create the model inputs (pixel_values, etc.)
    inputs = processor(images=image, return_tensors="pt")
    
    # 2. Generate the output tokens (using the inputs we just created)
    # We pass **inputs to unpack the dictionary (which contains pixel_values)
    output_ids = model.generate(**inputs, max_new_tokens=20)
    
    # 3. Decode the generated tokens back into a string
    caption = processor.decode(output_ids[0], skip_special_tokens=True)
    
    return caption

def process_frame(image_path):
    # 1. Vision (BLIP)
    caption = generate_caption(image_path)
    
    # 2. Text (OCR)
    text = extract_text(image_path)
    
    return caption, text

def log_analysis(filename, caption, detected_text):
    file_exists = os.path.isfile('analysis_log.csv')
    with open('analysis_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Frame Name', 'AI Caption','Detected Text'])
        writer.writerow([filename, caption, detected_text])

# Test it
frame_folder = "data/frames/BANANA (Animation Meme)"
for filename in os.listdir(frame_folder):
    if filename.endswith(".jpg"):
        path = os.path.join(frame_folder, filename)
        caption, detected_text = process_frame(path)
        print(f"Caption: {caption}")
        print(f"Detected Text: {detected_text}")
        log_analysis(filename, caption, detected_text)
        print(f"Logged: {filename} -> {caption} -> {detected_text}\n")
