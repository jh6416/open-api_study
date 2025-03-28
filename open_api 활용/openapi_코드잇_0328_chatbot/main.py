import os

from together import Together
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

SYSTEM_MESSAGE = """당신은 경험이 풍부한 셰프이자 요리 가이드입니다. 
초보 요리사도 쉽게 따라 할 수 있도록 재료 준비부터 조리법까지 단계별로 명확하게 설명하세요."""
# 상수는 모두 대문자 변하지 않기때문에
API_KEY = os.environ["API_KEY"]
BASE_URL = "https://api.together.xyz/v1"
DEFAULT_MODEL = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"

client = Together(api_key=API_KEY, base_url=BASE_URL)

messages = [
    {"role":'system','content':SYSTEM_MESSAGE}
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

def chatbot():
    print("Chatbot: 안녕하세요! 무엇을 도와드릴까요? (종료하려면 'quit' 또는 'exit'를 입력하세요.)\n)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit','exit']:
            break
        
        messages.append({"role":"user","content":user_input})
        print("\n==================================\n")
        print(f"messages : \n{messages}")
        print("\n==================================\n")
        # print(user_input)
        # # user_input을 messages에 추가해서 chat_completion_stream() 호출하기
        print("\nChatbot : ",end="")
        response = chat_completions_stream(messages)  # 답변을 계속 추가함
        print()
        
        messages.append({"role":"assistant","content":response})  # 대화에 맥락 유지에 핵심
        print("\n==================================\n")
        print(f"messages : \n{messages}")
        print("\n==================================\n")
        
        
chatbot()



