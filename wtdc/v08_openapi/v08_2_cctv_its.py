import urllib # URL 요청을 위한 라이브러리
import json # JSON 데이터 파싱용
import pandas as pd # 데이터 프레임 생성 및 데이터 처리용
import cv2 # 영상 처리용
import urllib.request # URL 요청

# 1. 인증 키 설정
key = "db5c00dc1fce45c49049bff225a0fea6"

# 2. 도로 유형 지정
# 'its'는 일반 도로 || 'ex'는 고속도로
Type = "its"

# 3. 경도, 위도 설정
minX = float(120.95)
maxX = float(127.02)

minY = float(30.55)
maxY = float(37.69)

# 4. 응답 데이터 형식 설정
getType = "json"

# 5. API 요청 URL 생성
url_cctv = f"https://openapi.its.go.kr:9443/cctvInfo?apiKey={key}&type={Type}&cctvType=1&minX={minX}&maxX={maxX}&minY={minY}&maxY={maxY}&getType={getType}"

# 6. 요청 및 응답 받기
response = urllib.request.urlopen(url_cctv)
# print(response)

# 7. 데이터 디코딩
json_str = response.read().decode("utf-8")
# print(json_str)

# 8. JSON 형태를 파이썬 딕셔너리 변환
json_obejct = json.loads(json_str)
# print(json_obejct)

# 9. 판다스 데이터 프레임 변환
cctv_play = pd.json_normalize(json_obejct["response"]["data"], sep='')
# 컬럼명 합칠 때 구분자 지정 (여기선 공백)

# print(cctv_play["cctvurl"])
# print(cctv_play["cctvname"])

# 10. 특정 CCTV 선택
test_url = cctv_play["cctvurl"][77]

# 11. 특정 CCTV 프레임 처리
cap = cv2.VideoCapture(test_url)
while cap.isOpened():
    success, frame = cap.read()
    
    cv2.namedWindow("OPENAPI", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("OPENAPU", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Q키를 눌러서 종료')
        break
    
# 12. 자원해제
cap.release()
cv2.destroyAllWindows()