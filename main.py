from fastapi import FastAPI, UploadFile, File
from whisper_utils import transcribe_audio
from bark_utils import generate_speech
from llama_client import generate_reply
import uuid
import os
from fastapi.responses import FileResponse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Access sensitive information securely
client_url = os.getenv("CLIENT_URL")

@app.post("/voice")
async def voice_interaction(audio: UploadFile = File(...)):
    temp_filename = f"temp_{uuid.uuid4().hex}.wav"
    
    with open(temp_filename, "wb") as f:
        f.write(await audio.read())

    user_text = transcribe_audio(temp_filename)
    print("User said:", user_text)
    print("client:", client_url)


    ai_reply = generate_reply(user_text, client_url)
    print("AI reply:", ai_reply)

    os.remove(temp_filename)

    return {
        "user_text": user_text,
        "ai_reply": ai_reply,
    }