import dotenv
import os
dotenv.load_dotenv(os.path.join(os.curdir,'.env'))
gemini_key=os.getenv('geminiapi')
