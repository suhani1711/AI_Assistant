import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"


def ask_ai(question, notes):

    prompt = f"""
You are an AI Study Assistant.

Answer the student's question using the study notes provided below.

Study Notes:
{notes}

Student Question:
{question}

Instructions:
- Give a clear and simple answer.
- Use the study notes as the main source.
- Explain difficult concepts in beginner-friendly language.
- Give an example when useful.
- If the answer is not available in the notes, say:
  "This information is not present in the provided notes."
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    data = response.json()

    return data["response"]