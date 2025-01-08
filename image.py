import google.generativeai as genai
import os
from PIL import Image
from io import BytesIO
from config import gemini_key

# Configuration
API_KEY = gemini_key

if not API_KEY:
    print("Please set the Gemini API KEY in the environment variables")
    exit()

# Configure Generative AI client
genai.configure(api_key=API_KEY, client_options={'api_endpoint': 'generativeai.googleapis.com'})


def generate_image_from_text(text_prompt, save_path=None):
    """Generates an image from a text prompt using the Gemini API."""

    # Set up the model and generate content
    model = genai.GenerativeModel('gemini-2.0-flash-experimental')  # Use your model name
    response = model.generate_content(text_prompt)

    if response.parts and response.parts[0].data:  # Check if image data is present
        image_bytes = response.parts[0].data
        if save_path:
            # Save image to a local file
            img = Image.open(BytesIO(image_bytes))
            img.save(save_path)
            print(f"Image saved to {save_path}")
            return save_path
        else:
            print("No save path was provided, returning image bytes only")
            return image_bytes
    else:
        print("No image data returned from the API")
        return None


if __name__ == "__main__":
    # Example usage:
    text_description = "A futuristic cityscape at night with flying cars and neon lights"  # Replace with your text prompt
    image_save_path = "generated_image.png"  # Set where to save image file

    generated_image = generate_image_from_text(text_description, image_save_path)

    if generated_image:
        print("Image generated")
        # You can now handle the image (either a path or raw bytes).
        # For example, if you saved it, the path is returned.
        # If you did not specify a save_path, then the raw image bytes
        # are returned which can be used with PIL or uploaded using other library.
    else:
      print("Failed to generate image")