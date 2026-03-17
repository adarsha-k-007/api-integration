import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Initialize client
client = Groq(api_key=api_key)


def query_groq(prompt):
    """
    Send prompt to Groq API and return response
    """

    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


def main():
    print(" ----------GROQ AI---------- \n")
    prompt = input("Enter your prompt: ")

    print("\nQuerying Groq API...\n")

    result = query_groq(prompt)

    print("Response:\n")
    print(result)


if __name__ == "__main__":
    main()