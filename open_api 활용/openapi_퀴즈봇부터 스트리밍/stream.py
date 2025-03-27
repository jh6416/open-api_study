import os

from together import Together
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

API_KEY = os.environ["API_KEY"]
BASE_URL = "https://api.together.xyz/v1"
DEFAULT_MODEL = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"

client = Together(api_key=API_KEY, base_url=BASE_URL)

messages = [
    {"role": "user","content":"아침에는 배를 먹어야 할까? 사과를 먹어야 할까?"},

]


def chat_completions(messages, model = DEFAULT_MODEL, temperature = 0.7 ,**kwargs):
    response = client.chat.completions.create(
        model = DEFAULT_MODEL,
        messages = messages,
        temperature = temperature,
        stream = False,
        **kwargs,
    )

    return response.choices[0].message.content


def chat_completions_stream(messages, model = DEFAULT_MODEL, temperature = 0.7 ,**kwargs):
    response = client.chat.completions.create(
        model = DEFAULT_MODEL,
        messages = messages,
        temperature = temperature,
        stream = True,
        **kwargs,
    )

    response_content = ""

    for chunk in response:
        chunk_content = chunk.choices[0].delta.content
        if chunk_content is not None:
            print(chunk_content, end="")
            response_content += chunk_content
    print()

    return response_content


print(f"\nstream 리턴값 \n{chat_completions_stream(messages,temperature=0.9)}")  # stream을 이용하여  모두 리턴함
    


