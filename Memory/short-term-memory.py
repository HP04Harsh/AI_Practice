import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

load_dotenv(Path(__file__).resolve().with_name(".env"))

api_key = os.getenv("GROQ_API_KEY") or os.getenv("Groq_API")
if not api_key:
    raise RuntimeError(
        "Set GROQ_API_KEY in Memory/.env. See .env.example for the format."
    )

client = Groq(api_key=api_key)
MODEL = "qwen/qwen3.8-27b"
SYSTEM_MESSAGE = {"role": "system", "content": "You are a helpful assistant."}
history: list[dict[str, str]] = []
MAX_HISTORY_MESSAGES = 10


def chat(query: str) -> str:
    query = query.strip()
    if not query:
        raise ValueError("Message cannot be empty.")

    messages = [
        SYSTEM_MESSAGE,
        *history,
        {"role": "user", "content": query},
    ]
    response = client.chat.completions.create(model=MODEL, messages=messages)
    reply = response.choices[0].message.content
    if reply is None:
        raise RuntimeError("Groq returned an empty response.")

    history.extend(
        [
            {"role": "user", "content": query},
            {"role": "assistant", "content": reply},
        ]
    )
    del history[:-MAX_HISTORY_MESSAGES]
    return reply


def main() -> None:
    print("Short-term memory chat. Type 'exit' to quit.")
    while True:
        query = input("You: ").strip()
        if query.lower() in {"exit", "quit"}:
            break
        if not query:
            continue
        print(f"Assistant: {chat(query)}")


if __name__ == "__main__":
    main()
