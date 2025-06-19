import requests
from config import GROQ_API_KEY, GROQ_BASE_URL, LLAMA_MODEL

def generate_llm_response(topic:str) -> str:

    messages = [{
        "role":"system",
        "content": (
            "Your are a fun fact generator. On the basis of topic you got provided, you just have to generate a fun fact on that."
            "You don't need to give xplanation or anything just generate one small fun fact."

        )
    },
    {
        "role":"user",
        "content":topic
    }
    ]

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload ={
        "model":LLAMA_MODEL,
        "messages":messages,
        "temperature":0.3,
        
    }
    response = requests.post(GROQ_BASE_URL, json=payload, headers=headers)
    response.raise_for_status()
    result = response.json()
    return result ["choices"][0]["message"]["content"]


