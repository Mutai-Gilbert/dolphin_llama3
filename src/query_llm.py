import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

LLAMA3_API_KEY = os.getenv("LLAMA3_API_KEY")
LLAMA3_ENDPOINT = os.getenv("LLAMA3_ENDPOINT")

def query_llm(prompt):
    headers = {
        'Authorization': f'Bearer {LLAMA3_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': prompt,
        'max_tokens': 150
    }
    response = requests.post(LLAMA3_ENDPOINT, headers=headers, json=data)
    return response.json()

if __name__ == "__main__":
    prompt = input("Enter your query: ")
    response = query_llm(prompt)
    print(response)
