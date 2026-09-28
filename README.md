# AI Text Generation API

## Project Description

This project is a simple AI API built using FastAPI. It accepts a text prompt through a POST endpoint and processes the input using a Python-based intelligence function.

## Technologies Used

* Python
* FastAPI
* Uvicorn
* Pydantic

## API Endpoint

### POST /generate

This endpoint accepts a text prompt from the user and returns a generated response.

### Request

```json
{
  "prompt": "Explain artificial intelligence in simple terms"
}
```

### Response

```json
{
  "prompt": "Explain artificial intelligence in simple terms",
  "answer": "Artificial Intelligence is a technology that enables computers to perform tasks that normally require human intelligence."
}
```

## How It Works

The user sends a text prompt to the `/generate` endpoint. FastAPI receives and validates the request, then passes the prompt to the Python-based intelligence function. The function generates a response, and FastAPI returns the result as a JSON response.

## Workflow

User Input → FastAPI Backend → Intelligence Function → Generated Output → JSON Response

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m uvicorn main:app --reload
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```
