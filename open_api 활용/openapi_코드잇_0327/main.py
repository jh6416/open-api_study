import os

from dotenv import load_dotenv, find_dotenv
from together import Together

_ = load_dotenv(find_dotenv())

API_KEY = os.environ["API_KEY"]
BASE_URL = "https://api.together.xyz/v1"
DEFAULT_MODEL = "gpt-4o-mini"

client = Together(api_key=API_KEY, base_url=BASE_URL)

response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    messages=[{"role": "user", "content": "안녕 반가워"}],
)

print(response.choices[0].message.content)