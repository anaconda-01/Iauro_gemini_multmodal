from google import generativeai as genai
from config import gemini_key

def Text_generation(prompt):
    genai.configure(api_key=gemini_key)
    model = genai.GenerativeModel(model_name='gemini-2.0-flash-exp')

    # Generate content with streaming enabled
    response = model.generate_content(prompt, stream=True)
    
    # Yield each chunk as it arrives
    for chunk in response:
        if hasattr(chunk, 'text'):
            yield chunk.text
        else:
            yield ""  # In case chunk does not contain text
