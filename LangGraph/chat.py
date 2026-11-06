from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list,add_messages]

graph_builder = StateGraph(State)


def chatbot(state: State):
    return {"messages": [{"role": "assistant", "content": "Hi, this is a message from Chatbot node"}]}

def weatherbot(state:State):
    return {"messages": [{"role": "assistant", "content": "Hi, this is a message from Weather node"}]}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("weatherbot", weatherbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "weatherbot")
graph_builder.add_edge("weatherbot", END)

graph = graph_builder.compile()

updated_state = graph.invoke(
    {"messages": [{"role": "user", "content": "Hi, my name is Piyush"}]}
)

print(updated_state)