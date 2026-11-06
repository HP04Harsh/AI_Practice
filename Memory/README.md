# Short-Term Memory Chat

A command-line chat example using Groq. It keeps the last five user/assistant
exchanges in memory for the current run. Conversation history is not saved
after the program exits.

## Requirements

- Python 3.10 or newer
- A Groq API key

## Setup

From this directory, install the packages into your current Python installation:

```powershell
python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your Groq API key:

```env
GROQ_API_KEY=your-groq-api-key
```

Keep `.env` private; it is excluded from Git. The script also accepts the
legacy `Groq_API` variable name.

## Run

```powershell
python .\short-term-memory.py
```

Type `exit` or `quit` to end the chat.
