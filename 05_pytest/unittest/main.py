from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the DACA Chatbot API! Access /docs for the API documentation."}

# User endpoint with optional query parameter 'role'
@app.get("/users/{user_id}")
def read_user(user_id: str, role: Optional[str] = Query("guest")):
    return {"user_id": user_id, "role": role}

# Request body schema for /chat/ endpoint
class ChatRequest(BaseModel):
    user_id: str
    text: str
    metadata: Dict[str, str]
    tags: Optional[List[str]] = []

# Response schema (optional, for clarity)
class ChatResponse(BaseModel):
    user_id: str
    reply: str
    metadata: Dict[str, str]

# Chatbot endpoint
@app.post("/chat/", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Message text cannot be empty")
    
    reply_text = f"Hello, {request.user_id}! You said: '{request.text}'. How can I assist you today?"
    return {
        "user_id": request.user_id,
        "reply": reply_text,
        "metadata": request.metadata
    }
