import os

from dotenv import load_dotenv
from groq import Groq

from ticket_model import Ticket

# Use an active Groq model identifier
MODEL = "openai/gpt-oss-120b"

schema = Ticket.model_json_schema()  # Get the JSON schema of the Ticket model

response={
     "type": "json_schema",
     "json_schema": schema
}

system_prompt = f"""You are a helpful assistant that generates a JSON object based on the
 following JSON schema:
{schema}
"""

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
     raise RuntimeError("Set GROQ_API_KEY in your environment or .env file.")

text="Hello my name is mushi,i have an samsumg s23 ultra and it is not working properly,my is xyz, my email is xyz@example.com. my phone is not turning on and i need help to fix it. please help me to fix it as soon as possible."

prompt = f"""Please generate a JSON object that adheres to the following schema:
{text}"""


client = Groq(api_key=api_key)

response = client.chat.completions.create(
      model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
)

    # Access the text output from choices
print("AI:", response.choices[0].message.content)


