from fastapi import FastAPI, HTTPException
import ollama

# FastAPI app initialize karein
app = FastAPI(title="Local Ollama FastAPI Bridge", version="1.0")

@app.get("/")
def home():
    return {"message": "FastAPI + Ollama server is running successfully!"}

@app.post("/chat")
def chat_with_ollama(prompt: str):
    try:
        # Local Ollama model ko request bhej rahe hain
        response = ollama.chat(model='qwen2.5-coder:0.5b', messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])

        # Model ka reply extract karke return karna
        ai_reply = response['message']['content']
        return {
            "status": "success",
            "prompt": prompt,
            "response": ai_reply
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))