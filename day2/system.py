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
    #System message to set the context for the AI model
    mess_system = {
        "role": "system",
        "content": "You are a helpful assistant who teach me a english vocabulary band 9 daily 3 words and give me a example sentence for each word. Please provide the words in a list format."
    }
    #temperature is set to 0.7 to allow for some creativity in the responses
    response = client.chat.completions.create(
        model=MODEL,
        messages=[mess_system, {"role": "user", "content": prompt}],
        temperature=2
    )
    
    # Access the text output from choices
    print("AI:", response.choices[0].message.content)

if __name__ == "__main__":
    main()