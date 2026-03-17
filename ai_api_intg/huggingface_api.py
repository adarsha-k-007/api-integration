import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("HUGGINGFACE_API_KEY")

# Initialize Hugging Face client
client = InferenceClient(
    model="openai/gpt-oss-20b",
    token=api_key
)


def query_huggingface(prompt):
    """Query Hugging Face conversational model"""

    try:

        response = client.chat_completion(
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=450,
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


def main():
    print(" ----------HUGGINGFACE AI---------- \n")
    prompt = input("Enter your prompt: ")

    print("\nQuerying Hugging Face API...\n")

    result = query_huggingface(prompt)

    print("Response:\n")
    print(result)


if __name__ == "__main__":
    main()