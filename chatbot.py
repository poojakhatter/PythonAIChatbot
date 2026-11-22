
# Import required libraries

import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Check API key
if not api_key:
    print("API Key not found!")
    print("Please check your .env file.")
    exit()

# Create Groq client
client = Groq(api_key=api_key)

print("--------------------------------")
print("       MY AI CHATBOT")
print("--------------------------------")
print("Ask me anything!")
print("Type 'exit' to stop the chatbot.")

# Store conversation history
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Answer in simple language."
    }
]

# Chatbot loop
while True:

    # Take input from user
    user_input = input("\nYou: ").strip()

    # Exit condition
    if user_input.lower() in ("exit", "quit"):
        print("\nBot: Goodbye! Have a nice day.")
        break

    # Ignore empty input
    if not user_input:
        continue

    # Add user message to history
    messages.append({
        "role": "user",
        "content": user_input
    })

    try:

        # Send request to Groq API
        response = client.chat.completions.create(

            model="openai/gpt-oss-120b",

            messages=messages

        )

        # Extract chatbot response
        bot_reply = response.choices[0].message.content

        # Display response
        print("\nBot:", bot_reply)

        # Store chatbot response
        messages.append({
            "role": "assistant",
            "content": bot_reply
        })

    except Exception as e:

        print("\nSomething went wrong!")
        print("Error Type:", type(e).__name__)
        print("Error Details:", str(e))

        # Remove failed user message
        messages.pop()
