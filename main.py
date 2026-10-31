from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llm_service import ask_ai
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app.mount("/static", StaticFiles(directory=STATIC_DIR),name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

class VoiceRequest(BaseModel):
    message: str

@app.get("/index.html")
async def home():
    return FileResponse(STATIC_DIR / "index.html")

@app.post("/chat")
async def chat(request: VoiceRequest):
    try:
        if not request.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        answer = ask_ai(request.message)
    
        return {"answer": answer}
    except HTTPException:
        raise

    except Exception as e:
        print("AI API Error: ", repr(e))
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
