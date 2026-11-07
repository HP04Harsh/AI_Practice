from dotenv import load_dotenv
import groq

load_dotenv()
client = groq.Client(api_key=os.getnev('Groq_API'))

response = client.chat.completions.create(
    model="gpt-4o-mini",   # ⭐ image support wala model hi chalega!
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Generate a caption for this image in about 50 words.",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/photo.jpg"},
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)


#local image
import base64

with open("photo.jpg", "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

url = f"data:image/jpeg;base64,{b64}"