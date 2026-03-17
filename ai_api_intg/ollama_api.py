import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def query_ollama(prompt):
    """Query Ollama local model"""

    try:

        payload = {
            "model": "tinyllama",
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(OLLAMA_URL, json=payload)

        if response.status_code != 200:
            return f"API Error: {response.text}"

        result = response.json()

        return result["response"]

    except Exception as e:
        return f"Error: {str(e)}"


def main():
    print(" ----------OLLAMA AI---------- \n")
    prompt = input("Enter your prompt: ")

    print("\nQuerying Ollama model...\n")

    result = query_ollama(prompt)

    print("Response:\n")
    print(result)


if __name__ == "__main__":
    main()