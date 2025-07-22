import os
from huggingface_hub import InferenceClient

print("TTI 실행을 시작합니다.")

# 토큰 등록
# os.environ["HF_TOKEN"]

# InferenceClient 객체 생성
client = InferenceClient(
    provider="auto", 
    api_key=os.environ["HF_TOKEN"],
)

# 질문 입력받기
answer = input("생성할 이미지를 설명해주세요. : ")

# 입력한 문장을 바탕으로 이미지 생성
image = client.text_to_image(
    answer, # 질문
    model="black-forest-labs/FLUX.1-dev", # 모델 지정
)

# 생성된 이미지를 저장
image.save("tti_image2.png")

# 완료 메시지 출력
print("전체 코드가 잘 실행되었음!")