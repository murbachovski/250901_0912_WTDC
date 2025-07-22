# pip install diffusers
# pip install transformers
# pip install accelerate
# 한번에 설치하는 방법
    # pip install diffuser transformers accelerate
    
# StableDiffusion 모델을 쉽게 불러와서 사용할 수 있는 클래스
from diffusers import StableDiffusionPipeline

print("코드가 성공적으로 실행 중")

# 사전 학습된 StableDiffustion 모델 로드
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5" # 모델 이름
)

# 모델을 사용할 디바이스로 이동
pipe = pipe.to("cpu")

# 이미지 생성할 프롬프트 입력
prompt = "nice bear"

# 프롬프트 기반 이미지 생성
image = pipe(prompt).images[0]

# 생성된 이미지를 파일로 저장
image.save("tti2_image.png")

# 완료 메시지 출력
print("코드가 성공적으로 실행되었음")
