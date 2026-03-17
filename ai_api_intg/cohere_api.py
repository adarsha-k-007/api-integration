import os
from dotenv import load_dotenv
import cohere

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("COHERE_API_KEY")

# Initialize Cohere client
co = cohere.Client(api_key)


def query_cohere(prompt):
    """Query Cohere model"""

    try:

        response = co.chat(
            message=prompt,
            model="command-a-03-2025",
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


def main():
    print(" ----------COHERE AI---------- \n")
    prompt = input("Enter your prompt: ")

    print("\nQuerying Cohere API...\n")

    result = query_cohere(prompt)

    print("Response:\n")
    print(result)


if __name__ == "__main__":
    main()