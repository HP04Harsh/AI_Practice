from dotenv import load_dotenv
from mem0 import Memory
import groq
import os

load_dotenv()
client = groq.Client(api_key=os.getenv('Groq_API'))

mem = Memory()

messages = [
    {"role": "user", "content": "Hi, main Harsh hoon aur ek AI Software Engineer hu. Mujhe pizza bohut pasand hai, burger bilkul nahi."},
    {"role": "assistant", "content": "Hello Harsh! Note kar liya 👍"},
]

result = mem.add(messages,user_id="harsh")
print(result)