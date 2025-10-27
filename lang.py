from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Check if key is loaded
api_key = os.getenv("OPENAI_API_KEY")  # ✅ FIXED NAME
print("API Key Loaded:", bool(api_key))

if not api_key:
    print("ERROR: OPENAI_API_KEY not found!")
    print("Please create a .env file with: OPENAI_API_KEY=your_api_key_here")
    exit(1)

# Initialize LangChain model
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(model="gpt-4o", temperature=0.7)

response = chat.invoke("Hello, how are you?")
print(response.content)
