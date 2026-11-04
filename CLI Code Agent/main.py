import os
import json
import groq
from dotenv import load_dotenv

load_dotenv()  
client = groq.Client(api_key=os.getenv("Groq_API"))

def run_command(command: str) -> str:
    """Takes System command as input and returns the output of the command."""
    try:
        result = os.popen(command).read()
        return result if result else "No output returned."
    except Exception as e:
        return f"Error occurred while executing the command: {str(e)}"

available_tools = {
    "run_command": run_command
}        

tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "run_command",
            "description": "Execute a system command and return its output.",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The system command to execute",
                    }
                },
                "required": ["command"],
            },
        },
    }
]

def run_coding_agent():
    print("🤖 CLI Code Agent Started! Ask anything.")
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant that can execute system commands. Always use the 'run_command' tool when asked to run a command."}
    ]

    while True:
        user_input = input("\nGive the command / ask to build: ")
        if user_input.lower() == "exit":
            print("Exiting the agent. Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        # API Call
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            tools=tools_schema,
            tool_choice="auto"
        )
        
        response_message = response.choices[0].message
        messages.append(response_message)

        # Check if the model wants to call a tool
        if response_message.tool_calls:
            for tool_call in response_message.tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)
                
                print(f"🛠️ Tool Called: {tool_name} with args: {tool_args}")

                if tool_name in available_tools:
                    tool_output = available_tools[tool_name](**tool_args)
                    print(f"📂 Output:\n{tool_output}")
                    
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": tool_output
                    })

            # Get final response after tool execution
            second_response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages
            )
            
            final_content = second_response.choices[0].message.content
            print(f"🤖 AI: {final_content}")
            messages.append({"role": "assistant", "content": final_content})
            
        else:
            print(f"🤖 AI: {response_message.content}")
        
if __name__ == "__main__":
    run_coding_agent()