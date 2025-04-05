# import numpy as np
# from bark import SAMPLE_RATE, generate_audio
# from scipy.io.wavfile import write as write_wav
# import nltk
# nltk.download("punkt_tab")
# from nltk.tokenize import sent_tokenize
# import uuid

# def generate_speech(text):
#     sentences = sent_tokenize(text)
#     full_audio = np.array([], dtype=np.float32)

#     for sentence in sentences:
#         audio = generate_audio(sentence, history_prompt="v2/en_speaker_9")
#         full_audio = np.concatenate((full_audio, audio))

#     # output_path = "static/output.wav"
    # filename = f"audio_reply_{uuid.uuid4().hex}.wav"
#     write_wav(filename, SAMPLE_RATE, full_audio)
#     return filename



# Using local TTS
import subprocess
import uuid

def generate_speech(text):
    audio_filename = f"audio_reply_{uuid.uuid4().hex}.aiff"
    
    # Use macOS built-in TTS
    subprocess.run(["say", "-v", "Samantha", "-o", audio_filename, text])
    # subprocess.run(["say", "-o", audio_filename, text])
    
    # Optionally convert to WAV or MP3 (depending on your Flutter audio player)
    wav_output = audio_filename.replace(".aiff", ".wav")
    subprocess.run(["ffmpeg", "-y", "-i", audio_filename, wav_output])
    
    return wav_output
