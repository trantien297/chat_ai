from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
# from elevenlabs import play
import os

load_dotenv()

elevenlabs = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)

def text_to_speech(text, audio_path):
    audio = elevenlabs.text_to_speech.convert(
        text=text,
        voice_id="ZF6FPAbjXT4488VcRRnw",
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
    )
  
    # Ghi file mp3
    with open(audio_path, "wb") as f:
        for chunk in audio:
            f.write(chunk)

    return audio_path

    # play(audio)