import os
import requests
from dotenv import load_dotenv
import json
import groq
from pydantic import BaseModel, Field

load_dotenv()
client = groq.Client(api_key=os.getenv("Groq_API"))

class OutputFormat(BaseModel):
    city: str = Field(..., description="The name of the city")
    weather: str = Field(..., description="The current weather information for the city")

# 1. Weather Tool Function
def get_weather(city: str) -> str:
    url = f"https://wttr.in/{city.lower()}?format=3"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Hum ek JSON formatted string return kar rahe hain
            return OutputFormat(city=city, weather=response.text.strip()).model_dump_json()
        else:
            return OutputFormat(city=city, weather="Could not retrieve weather data.").model_dump_json()
    except Exception as e:
        return OutputFormat(city=city, weather=f"Error occurred: {str(e)}").model_dump_json()

# Available tools map
available_tools = {
    "get_weather": get_weather
}

# 2. Tools Schema for Groq/OpenAI
tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a given city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city name, e.g. Delhi, Mumbai, Gondia",
                    }
                },
                "required": ["city"],
            },
        },
    }
]

def run_agent():
    print("🤖 Weather Agent Started! Ask anything.")
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant that provides weather information. Always use the 'get_weather' tool when asked about weather."}
    ]

    while True:
        query = input("\nEnter a city name (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            print("Exiting the Weather Agent. Goodbye!")
            break

        messages.append({"role": "user", "content": query})

        # API Call
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,
            tools=tools_schema,
            tool_choice="auto",
            response_format=OutputFormat
        )
        
        response_message = response.choices[0].message
        messages.append(response_message)

        # Check if the model wants to call a tool
        if response_message.tool_calls:
            for tool_call in response_message.tool_calls:
                tool_name = tool_call.function.name
                # Parse arguments safely from JSON string
                tool_args = json.loads(tool_call.function.arguments)
                
                print(f"🛠️ Tool Called: {tool_name} with args: {tool_args}")

                # Execute local function if it exists
                if tool_name in available_tools:
                    # Yahan function call ho raha hai aur string output mil raha hai
                    tool_output = available_tools[tool_name](**tool_args)
                    
                    # Append tool response back to messages
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": tool_output
                    })

            # Get final response from model after providing tool output
            second_response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=messages,
                response_format=OutputFormat
            )
            
            final_content = second_response.choices[0].message.content
            print(f"🤖 Bot: {final_content}")
            messages.append({"role": "assistant", "content": final_content})
            
        else:
            print(f"🤖 Bot: {response_message.content}")

if __name__ == "__main__":
    run_agent()