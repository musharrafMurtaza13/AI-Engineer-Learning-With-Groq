import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Fetch all models available to your account
models = client.models.list()
for model in models.data:
    print(model.id)



# whisper-large-v3-turbo
# openai/gpt-oss-20b
# meta-llama/llama-prompt-guard-2-86m
# openai/gpt-oss-safeguard-20b
# allam-2-7b
# canopylabs/orpheus-arabic-saudi
# whisper-large-v3
# canopylabs/orpheus-v1-english
# qwen/qwen3.8-27b
# openai/gpt-oss-120b
# meta-llama/llama-prompt-guard-2-22m