import os
import requests
from dotenv import load_dotenv
from groq import Groq
from huggingface_hub import InferenceClient
import cohere

# Load env variables
load_dotenv()

# API Keys
groq_key = os.getenv("GROQ_API_KEY")
hf_key = os.getenv("HUGGINGFACE_API_KEY")
cohere_key = os.getenv("COHERE_API_KEY")

# Clients
groq_client = Groq(api_key=groq_key)
hf_client = InferenceClient(model="openai/gpt-oss-20b", token=hf_key)
co = cohere.Client(cohere_key)


# ---------------- GROQ ----------------
def query_groq(prompt):
    try:
        response = groq_client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


# ---------------- HUGGINGFACE ----------------
def query_hf(prompt):
    try:
        response = hf_client.chat_completion(
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


# ---------------- COHERE ----------------
def query_cohere(prompt):
    try:
        response = co.chat(
            message=prompt,
            model="command-a-03-2025"
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"


# ---------------- OLLAMA ----------------
def query_ollama(prompt):
    try:
        url = "http://localhost:11434/api/generate"

        payload = {
            "model": "tinyllama",
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(url, json=payload)

        if response.status_code != 200:
            return f"Error: {response.text}"

        return response.json()["response"]

    except Exception as e:
        return f"Error: {e}"


# ---------------- MAIN MENU ----------------
def main():

    while True:
        print("\n====== MULTI API QUERY ======")
        print("1. Groq")
        print("2. HuggingFace")
        print("3. Cohere")
        print("4. Ollama")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "5":
            print("Exiting...")
            break

        prompt = input("\nEnter your prompt: ")

        print("\nProcessing...\n")

        if choice == "1":
            print(query_groq(prompt))

        elif choice == "2":
            print(query_hf(prompt))

        elif choice == "3":
            print(query_cohere(prompt))

        elif choice == "4":
            print(query_ollama(prompt))

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()