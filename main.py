from fastapi import FastAPI, UploadFile, File
from whisper_utils import transcribe_audio
from bark_utils import generate_speech
from llama_client import generate_reply
import uuid
import os
from fastapi.responses import FileResponse

app = FastAPI()

@app.post("/voice")
async def voice_interaction(audio: UploadFile = File(...)):
    temp_filename = f"temp_{uuid.uuid4().hex}.wav"
    
    with open(temp_filename, "wb") as f:
        f.write(await audio.read())

    user_text = transcribe_audio(temp_filename)
    print("User said:", user_text)

    ai_reply = generate_reply(user_text)
    print("AI reply:", ai_reply)

    audio_reply_path = generate_speech(ai_reply)

    os.remove(temp_filename)

    return {
        "user_text": user_text,
        "ai_reply": ai_reply,
        "audio_url": f"/audio/{audio_reply_path}"
    }

@app.get("/audio/{filename}")
def get_audio(filename: str):
    return FileResponse(path=filename, media_type='audio/wav', filename=filename)