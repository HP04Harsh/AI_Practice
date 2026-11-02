import groq
import os
import dotenv

dotenv.load_dotenv()
client  = groq.Client(api_key=os.getenv("Groq_API"))

# zero_shot_prompt = """ You should ONLY answer coding-related questions.
# Do not answer anything else. Your name is Alexa.
# If the user asks something other than coding, simply say: 'Sorry, I can only help with coding."""

# few_shot_prompt = """ You are a coding assistant named Alexa. Answer only programming queries.
# Examples:
# User: Can you explain the (A + B)^2 formula?
# Assistant: Sorry, I can only help with coding-related questions.

# User: Write a code in Python for adding two numbers.
# Assistant:
# def add(a, b):
#     return a + b
# """

cot_system_prompt = """
You are an expert Maths Tutor. You are very good at solving mathematical problems and explaining the steps clearly.
Always break down complex problems step-by-step using this format:

Step: plan -> Detail your thought process / mathematical step.
Step: output -> Provide the final answer once finished.

Example:
User: Calculate 2 + 3 * 5 / 10
Assistant:
Plan: Solve using BODMAS. First perform multiplication (3 * 5 = 15).
Plan: Next perform division (15 / 10 = 1.5).
Plan: Now perform addition (2 + 1.5 = 3.5).
Output: 3.5
"""

chat_completion = client.chat.completions.create(
    model = "openai/gpt-oss-120b",
    messages = [
        {"role" : "system", "content": cot_system_prompt},
        {"role" : "user", "content": "solve 5*5+[3-6*3]"}
    ]
)

print(chat_completion.choices[0].message.content)