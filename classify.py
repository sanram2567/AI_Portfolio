from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load a dedicated Captioning model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image_path):
    image = Image.open(image_path).convert('RGB')
    
    # Let the model generate the text itself!
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    
    return processor.decode(out[0], skip_special_tokens=True)

# Test it
print(f"AI Caption: {generate_caption('data/frames/BANANA (Animation Meme)/frame_0.jpg')}")