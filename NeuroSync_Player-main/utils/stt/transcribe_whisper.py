import requests

OPENAI_API_KEY = "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"  # Use the API key from your environment

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
