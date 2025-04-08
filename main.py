from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENROUTER_API_KEY = "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"  

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5500",  
        "X-Title": "My Chatbot",
    }

    payload = {
        "model": "openchat/openchat-7b",  
        "messages": [{"role": "user", "content": user_message}]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
    result = response.json()

    return {"response": result["choices"][0]["message"]["content"]}


# vicorn main:app --reload

