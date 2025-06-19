import os
from dotenv import load_dotenv

load_dotenv()

# here we get load values from .env
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
GROQ_BASE_URL=os.getenv("GROQ_BASE_URL")
LLAMA_MODEL=os.getenv("LLAMA_MODEL")