from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

print("=================================")
print("AI Student Assistant Chatbot")
print("Type 'quit' to exit")
print("=================================")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )

        print("\nBot:", response.text)

    except Exception as e:
        print("\nError:", e)