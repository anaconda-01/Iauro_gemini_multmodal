from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, HTMLResponse
from gen_text import Text_generation
import uvicorn
from fastapi.templating import Jinja2Templates
template=Jinja2Templates(directory="templates")
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return template.TemplateResponse("index.html",{"request":request})

@app.get("/chat", response_class=StreamingResponse)
async def chat(prompt: str):
    # The prompt comes from the query parameter
    response = Text_generation(prompt)
    
    # Return the response as a StreamingResponse
    return StreamingResponse(response, media_type="text/plain")

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8001)
