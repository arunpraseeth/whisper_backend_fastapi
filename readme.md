📦 1.1 Create a Python Virtual Environment
python3 -m venv venv
source venv/bin/activate

📦 1.2 Install Required Packages

🧠 1.3 FastAPI App Structure
backend/
│
├── main.py                 # FastAPI app
├── whisper_utils.py        # Whisper functions
├── bark_utils.py           # Bark functions
├── models/
│   └── your LLM model

✍️ 1.4 Write FastAPI Code (main.py)

🔊 1.5 Whisper Utility (whisper_utils.py)

🧠 1.6 Connect to LLM

!!!!!!!!!! If you donot have GPU proceed to 1.8 (bark requires GPU if not it will be slow)!!!!!!!!!!

🔈 1.7 Bark Utility (bark_utils.py) (In order to make the process faster - need a GPU)
    * This will download a 5GB file for the first time.
    * There will be a issue regarding weights_load:
        torch.load() now loads only weights for safety and we have to specify that in bark - generation.py file (making it safe)
        Under lib/python3.9/site-packages/bark/
            generation.py
                change: checkpoint = torch.load(ckpt_path, map_location=device) to checkpoint = torch.load(ckpt_path, map_location=device, 
                weights_only = False)
    * Again it will download few more files

    1.8 - Update - I do not have GPU and so it's taking more time to synthesize text to speech, so I'm using native TTS in my mobile.


📱 STEP 2: Connect Flutter to FastAPI
🗣️ 2.1 Flutter UI Sends Voice