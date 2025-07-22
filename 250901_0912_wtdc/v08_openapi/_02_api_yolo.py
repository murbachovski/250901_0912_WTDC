# # OpenAPI 설명
# from IPython.display import Image, display
# explain = "C:/Users/DSU/Desktop/kdt/v05_openapi/api.png"
# display(Image(filename=explain))

# 필요한 모듈 불러오기
import urllib
import json
import pandas as pd
import cv2
import urllib.request
from ultralytics import YOLO

# 1. Open API 인증키 (발급받은 받은 키를 입력)
key = ""

# 2. 도로 유형 (its : 일반 도로, ex : 고속도로)
Type = ""

# 3. CCTV 데이터 요청을 위한 지리적 범위 설정(경도, 위도)
minX = float(120.95)
maxX = float(127.02)
minY = float(30.55)
maxY = float(37.69)

# 4. 응답 데이터 포맷 (json 또는 xml 가능)
getType = "json"

# 5. 위에서 설정한 값들을 조합하여 CCTV 정보 요청용 URL 생성
url_cctv = f"https://openapi.its.go.kr:9443/cctvInfo?apiKey={key}&type={Type}&cctvType=1&minX={minX}&maxX={maxX}&minY={minY}&maxY={maxY}&getType={getType}"

# 6. 생성한 URL로 API 요청 후 응답
response = urllib.request.urlopen(url_cctv)
# => 해당 URL로 GET 요청 보내고 서버 응답 받음!!

print(response)

# 7. 응답 받은 데이터를 utf-8형태로 변환
json_str = response.read().decode("utf-8")
# => byte 형태로 받은 응답을 UTF-8 문자열로 변환

# 8. JSON 문자열을 파이썬 딕셔너리로 변환
json_object = json.loads(json_str)

print(json_object)

# 9. pandas DataFrame으로 변환
cctv_play = pd.json_normalize(json_object["response"]["data"], sep='')
# => 쉽게 분석하거나 필터링!!

print(cctv_play["cctvurl"])

print(cctv_play['cctvname'])

test_url = cctv_play['cctvurl'][99]

# 비디오 경로 설정
cap = cv2.VideoCapture(test_url)

model = YOLO("yolo11n.pt")

# 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("비디오 경로 없음")
        break
    
    # 모델 예측
    results = model(frame)
    
    annotated_frame = results[0].plot()
    
    # 영상 창 조절
    cv2.namedWindow("OPENAPI", cv2.WINDOW_NORMAL)
    # 영상 창 출력
    cv2.imshow("OPENAPI", annotated_frame)
    # q 키 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('q키 눌러서 종료')
        break
    
cap.release()
cv2.destroyAllWindows()