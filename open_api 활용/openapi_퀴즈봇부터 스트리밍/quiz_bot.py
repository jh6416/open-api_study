import os

from together import Together
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

API_KEY = os.environ["API_KEY"]
BASE_URL = "https://api.together.xyz/v1"
DEFAULT_MODEL = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"

client = Together(api_key=API_KEY, base_url=BASE_URL)

# user(질문을 하는 사용자), assistant(답변을 해주는 ai), system(전체적인 맥락이나 지시를 설정)
# messages = [
#     {"role": "user","content": "알리오올리오 파스타를 만들고 싶어. 레시피를 알려줘"},
#     {"role":"assistant","content":'''알리오올리오 파스타는 이탈리아의 전통 파스타 요리 중 하나로, 간단하지만 맛있는 레시피입니다. 다음은 알리오올리오 파스타를 만드는 방법입니다.

#     **재료:**

#     * 파스타 (스파게티나 펜네 등) - 200g
#     * 마늘 - 3-4쪽
#     * 올리브 오일 - 1/4컵
#     * 고춧가루 - 1/2티스푼
#     * 소금 - 1/2티스푼
#     * 후추 - 1/4티스푼
#     * 파마산 치즈 - 1/4컵 (생략 가능)
#     * 신선한 파슬리 - 1/4컵 (생략 가능)

#     **조리 방법:**

#     1. **파스타를 삶는다**: 큰 냄비에 물을 채우고, 소금을 넣어 끓인다. 파스타를 넣고, 알덴테(조리 시간의 2/3 정도)로 삶는다. 물을 버리고, 파스타를 건져낸다.
#     2. **마늘을 다진다**: 마늘을 잘게 다진다.
#     3. **올리브 오일을 데운다**: 큰 프라이팬에 올리브 오일을 넣고, 중불로 데운다.
#     4. **마늘을 넣는다**: 다진 마늘을 프라이팬에 넣고, 약 1-2분간 볶는다. 마늘의 향이 올라오면, 고춧가루를 넣는다.
#     5. **고춧가루를 볶는다**: 고춧가루를 약 30초간 볶는다.
#     6. **파스타를 넣는다**: 삶은 파스타를 프라이팬에 넣고, 잘 섞는다.
#     7. **소금과 후추를 넣는다**: 소금과 후추를 넣고, 잘 섞는다.
#     8. **파마산 치즈와 파슬리를 넣는다**: 파마산 치즈와 신선한 파슬리를 넣고, 잘 섞는다.
#     9. **완성**: 알리오올리오 파스타를 완성한다.

#     **팁:**

#     * 마늘의 양을 조절할 수 있습니다. 마늘을 더 많이 넣으면, 더 강한 맛이 나옵니다.
#     * 고춧가루를 넣지 않으면, 알리오올리오 파스타의 전통적인 맛이 나지 않을 수 있습니다.
#     * 파마산 치즈와 파슬리는 생략할 수 있습니다.'''},
#     {"role": "user","content": "4인분 레시피를 알려줘"},
# ]

# system을 사용해 맥락을 지정
# messages_1 = [
#     {"role": "system","content": '친구처럼 반말하세요.'},
#     {"role": "user","content": "알리오올리오 파스타를 만들고 싶어. 레시피를 알려줘"},
# ]

# messages_2 = [
#     {"role": "user","content": "알리오올리오 파스타를 만들고 싶어. 레시피를 알려줘"},
# ]


# 퀴즈봇 만들기  system으로 시작할때 퀴즈를 내는 맥락 작성
# quiz = [
#     {"role":"system", "content":'''당신은 친절하고 재미있는 지리 퀴즈 진행자입니다. 사용자가 '시작'이라고 입력하면 지리 퀴즈를 내주세요.\n
#     사용자가 답을 맞히면 축하 메시지를 보내고 다음 문제를 출제하세요. 답을 틀리면 정답을 알려주고 다음 문제를 출제하세요. 질문은 명확하고 재미있게 구성하세요.'''},
#     {"role": "user", "content": "시작"},
#     {"role": "assistant", "content": 
#     ''' 지리 퀴즈를 시작합니다. 

#     첫 번째 문제입니다.

#     세계에서 가장 큰 사막은 어디에 위치하고 있습니까?

#     A) 사하라 사막 (아프리카)
#     B) 고비 사막 (아시아)
#     C) 아타카마 사막 (남아메리카)
#     D) 그레이트 빅토리아 사막 (오스트레일리아)

#     답을 입력해 주세요!'''},
#     {"role": "user", "content": "A"},
#     ]




# def chat_completions(messages, model = DEFAULT_MODEL):
#     response = client.chat.completions.create(
#         model = DEFAULT_MODEL,
#         messages = messages,
#     )

#     return response.choices[0].message.content
    
# print(chat_completions(messages)) # 기본

# print(f"시스템 메시지 포함:\n{chat_completions(messages_1)}")
# print("\n=================================================\n")
# print(f"시스템 메시지 미포함:\n{chat_completions(messages_2)}")

# print(chat_completions(quiz))  퀴즈봇


