from dotenv import load_dotenv
import groq

def audiotrack(audio:str)->str:
    with open(audio, "rb") as file:
        result = client.audio.transcriptions.create(
            model="whisper-1",
            file=file
        )
    return result.text


print(audiotrack("audio.mp3"))