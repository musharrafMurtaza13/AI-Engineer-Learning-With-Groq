import os
from dotenv import load_dotenv
from groq import Groq

# Use an active Groq model identifier
MODEL = "openai/gpt-oss-120b" 

def main() -> None:
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("Set GROQ_API_KEY in your environment or .env file.")

    prompt = input("You: ")
    client = Groq(api_key=api_key)
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    
    # Access the text output from choices
    print("AI:", response.choices[0].message.content)

if __name__ == "__main__":
    main()