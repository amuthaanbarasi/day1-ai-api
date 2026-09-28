from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str


def generate_ai_response(prompt: str) -> str:
    prompt_lower = prompt.lower()

    if "artificial intelligence" in prompt_lower:
        return (
            "Artificial Intelligence is a technology that enables "
            "computers to perform tasks that normally require human intelligence."
        )

    if "machine learning" in prompt_lower:
        return (
            "Machine Learning is a branch of Artificial Intelligence "
            "that enables computers to learn patterns from data."
        )

    if "deep learning" in prompt_lower:
        return (
            "Deep Learning is a type of Machine Learning that uses "
            "neural networks with multiple layers."
        )

    return f"I received your prompt: '{prompt}'."


@app.get("/")
def home():
    return {
        "message": "AI Text Generation API is running"
    }


@app.post("/generate")
def generate_text(request: PromptRequest):
    answer = generate_ai_response(request.prompt)

    return {
        "prompt": request.prompt,
        "answer": answer
    }