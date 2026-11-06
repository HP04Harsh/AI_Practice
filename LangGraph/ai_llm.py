from typing import Annotated
from typing_extensions import TypedDict
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

load_dotenv()  # API key ke liye!


class State(TypedDict):
    messages: Annotated[list, add_messages]


# Groq model (set GROQ_API_KEY in .env)
llm = init_chat_model("qwen/qwen3.8-27b", model_provider="groq")


def chatbot(state: State):
    # State ke saare messages LLM ko do, uska jawab return kar do
    response = llm.invoke(state["messages"])
    return {"messages": response}


def sample_node(state: State):
    return {"messages": "Sample message appended"}


builder = StateGraph(State)
builder.add_node("chatbot", chatbot)
builder.add_node("sample", sample_node)
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", "sample")
builder.add_edge("sample", END)
graph = builder.compile()

final_state = graph.invoke(
    {"messages": [{"role": "user", "content": "Hi, my name is Piyush"}]}
)
for msg in final_state["messages"]:
    print("-", msg.content)