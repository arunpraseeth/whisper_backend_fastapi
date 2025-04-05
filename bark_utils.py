from bark import generate_audio
import scipy.io.wavfile
import numpy as np
import uuid

def generate_speech(text):
    audio_array = generate_audio(text)
    filename = f"audio_reply_{uuid.uuid4().hex}.wav"
    scipy.io.wavfile.write(filename, 22050, audio_array)
    return filename