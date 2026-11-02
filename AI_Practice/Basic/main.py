import os

import groq
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

load_dotenv()  # Load environment variables from .env file
client = groq.Client(api_key=os.getenv("Groq_API"))  # Use the API key from the environment variable
console = Console()

messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful assistant. Answer the user's question clearly using Markdown. "
            "Use headings, lists, tables, and fenced code blocks when they improve readability. "
            "End with a relevant follow-up question."
        )
    }
]

console.print("[bold cyan]Groq Continuous Chat[/bold cyan] [dim](type 'exit' to quit)[/dim]\n")

while True:
    user_input = console.input("[bold green]You:[/bold green] ")
    if user_input.lower() == "exit":
        console.print("[dim]Exiting the chat. Goodbye![/dim]")
        break

    messages.append({"role": "user", "content": user_input})

    chat_completion = client.chat.completions.create(
        model = "openai/gpt-oss-120b",
        messages = messages
    )

    ai_response = chat_completion.choices[0].message.content
    console.print()
    console.print(
        Panel(
            Markdown(ai_response),
            title="[bold cyan]AI[/bold cyan]",
            border_style="cyan",
            padding=(1, 2),
        )
    )
    console.print()

    messages.append({"role": "assistant", "content": ai_response})
