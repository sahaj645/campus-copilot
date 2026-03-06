from fastapi import FastAPI
from ai_router import process_query

app = FastAPI()

@app.post("/chat")

def chat(data: dict):

    message = data["message"]

    category = process_query(message)

    return {
        "category": category,
        "response": f"Request routed to {category} service"
    }