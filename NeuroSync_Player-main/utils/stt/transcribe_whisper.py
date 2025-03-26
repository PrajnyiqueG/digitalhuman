import requests
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def transcribe_audio(audio_bytes):
    """Transcribe audio using OpenAI Whisper API."""
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    files = {
        "file": ("audio.wav", audio_bytes, "audio/wav")
    }
    data = {
        "model": "whisper-1",
        "response_format": "json",
        "language": "en"  # Change this if needed
    }
    try:
        response = requests.post(
            "https://api.openai.com/v1/audio/transcriptions",
            headers=headers,
            files=files,
            data=data
        )
        if response.status_code == 200:
            response_data = response.json()
            transcription = response_data.get("text", "").strip()
            return transcription, None
        print(f"Error: OpenAI API returned status {response.status_code}")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with exception: {e}")
    return None, None
