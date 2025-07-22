# 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

# 환경 변수 설정 => 민감한 정보를 환경 변수로 안전하게 다루기 위해서
import os
# HuggingFace를 사용하기 위한 라이브러리
from huggingface_hub import InferenceClient

# 토큰 키 등록
# os.environ["HF_TOKEN"]

# InferenceClient 생성
client = InferenceClient(
    provider="auto", # 어떤 API 제공자인지 확인
    api_key=os.environ["HF_TOKEN"], # 토큰 키 확인
)

# 사용자에게 질문을 입력 받기
answer = input("질문을 입력해주세요. : ") # => 유저로 부터 질의 내용을 입력 받음

# DeepSeek-R1-0528의 모델에 메시지를 보내 답변을 요청!
completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1-0528",
    messages=[
        {
            "role": "user", # 챗봇 대화 형식
            "content": answer # 질문
        }
    ],
)

# 질문에 대한 답을 출력
print("===========================")
print(completion.choices[0].message)
print("===========================")