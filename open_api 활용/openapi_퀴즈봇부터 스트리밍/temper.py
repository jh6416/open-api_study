import os

from together import Together
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

API_KEY = os.environ["API_KEY"]
BASE_URL = "https://api.together.xyz/v1"
DEFAULT_MODEL = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"

client = Together(api_key=API_KEY, base_url=BASE_URL)

messages = [
    {"role": "user","content":"AI가 세상을 지배하는 SF소설의 첫 두 문단을 작성해줘."},

]


def chat_completions(messages, model = DEFAULT_MODEL, temperature = 0.7, **kwargs):
    response = client.chat.completions.create(
        model = DEFAULT_MODEL,
        messages = messages,
        temperature = temperature,
        **kwargs,
        # top_p
        # frequency_penalty
        # presence_penalty
    )

    return response.choices[0].message.content


# print(f"temperature=0:\n{chat_completions(messages, temperature=0)}")
# print("\n========================================================\n")
# print(f"temperature=1.5:\n{chat_completions(messages, temperature=1.5)}")  
# temperature 0에서 1 사용 권장

print(chat_completions(messages, top_p=0.7, frequency_penalty = 0.5,presence_penalty=0.5))  
# 원하는 답변을 얻지 못했다면 이런식으로 파라미터를 조절해보세요.




