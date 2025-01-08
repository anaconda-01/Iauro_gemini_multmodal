import google.generativeai as genai
import os
from config import gemini_key  # Ensure that gemini_key is correctly imported and contains your API key

# Set the path for your media file
media = os.path.join(os.curdir, "nikhil.mp3")
print(f"Media file path: {media}")

# Ensure the API key is set correctly
genai.configure(api_key=gemini_key)  # Pass the API key to configure

# Upload the audio file
myfile = genai.upload_file(media)
print(f"Uploaded file: {myfile}")

# Specify the model name and generate content
model = genai.GenerativeModel(model_name='gemini-2.0-flash-exp')
result = model.generate_content([myfile, "Describe this audio clip"])
print(f"Generated content: {result.text}")
