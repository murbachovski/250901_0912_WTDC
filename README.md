# WTDC(Woori_Talent_Development_Center) 

### 강의 주제
```
통합(인파 밀집 위험 예측 경보 시스템 + 교차로 교통 장애물 및 이벤트 감지 시스템)
```

### 강의 내용

```
1. 개발 요구사항 분석 및 기술 분석
교차로 교통 장애물 및 이벤트 감지 시스템의 필요성과 기술적 요구사항을 분석

2. 목표 설정 및 기획서 작성
프로젝트의 목표 설정 및 기획서 작성

3. 데이터 수집 및 전처리 모듈 개발
교차로 데이터 수집 및 전처리 작업 수행

4. 객체 감지 및 분류 모델 모듈 개발
객체 감지를 위한 모델 개발 및 분류 기능 구현

5. 실시간 처리 및 시각화 모듈 개발
실시간 데이터 처리를 위한 모듈 개발 및 결과 시각화

6. 이벤트 감지 및 분류 모듈 개발
이벤트 감지를 위한 모듈 개발 및 분류 기능 구현

7. 모델 성능 평가 및 성능 개선
개발된 모델의 성능 평가 및 개선 작업 수행

8. 교차로 교통 장애물 감지 모듈 개발
교차로 교통 장애물 감지를 위한 모듈 개발

9. Dashboard 연동, 테스트 및 디버깅
Dashboard와의 연동, 시스템 테스트 및 디버깅

10. 프로젝트 결과
프로젝트 PPT 발표
```

### 강의 시간

```
1) 09:30 ~ 10:20(50분)
2) 10:30 ~ 11:20(50분)
3) 11:30 ~ 12:20(50분)
4) 12:30 ~ 13:20(50분)
점심 13:20 ~ 14:10(점심)
5) 14:10 ~ 15:00(50분)
6) 15:10 ~ 16:00(50분)
7) 16:10 ~ 17:00(50분)
8) 17:10 ~ 18:00(50분)
(8교시, 총 400분)
```

### 강의 목차(Beta)

```
v0_Install anaconda/
→ Anaconda 설치 및 환경 설정

v1_Install vscode/
→ VS Code 설치 및 개발 환경 구성

v2_Basic python/
→ Python 기초 문법 및 실습

v3_Yolo 기초/
→ YOLO 객체 탐지 모델 추론 및 활용

v4_TWilio/
→ Twilio API를 활용한 문자(SMS) 알림 기능 구현

v5_OpenCV2/
→ OpenCV를 이용한 이미지 처리 실습

v6_Data
│
├── v6_1_Data/
│ → 공공데이터 포털 활용 및 교통/환경 데이터 수집
│
├── v6_2_Get Local Data/
│ → Local 이미지 수집 및 자동 이미지 저장 기능 구현
│
└── v6_3_OpenAPI/
     → 공공기관(OpenAPI) 연계 실시간 정보 수집

v7_YOLO 심화/
→ Solution 탐색
├── classify
├── train classify
├── detect
├── params
├── alarm
├── distance
├── sahi
├── heatmap
├── region
├── get region
├── speed
├── blurr
├── crop
├── in and out
├── line
├── YOLOE
├── multi thread
├── model.fuse()
├── Streamlit YOLO
└── OpenVINO int8

v8_Web
├── v8_3_Streamlit/
     → Streamlit을 활용한 YOLO 객체 탐지 실시간 시각화 대시보드 구현

v8_4_Plus/
    → HuggingFace
    → ngrok
    → pip free > requirements.txt
    → pip install pipreqs
    → model.fuse()
    → YOLOE
    → OpenVINO
    → YOLO_Streamlit
    → Export TensorRT
```

### API_KEY
```
db5c00dc1fce45c49049bff225a0fea6
```

## 추가 공유 내용
### 1. requirements.txt 생성 라이브러리 piqres
```
1. 기존 pip freeze 와 비교
2. pip freeze > requirements.txt
3. pip install pipreqs
3-1. pipreqs .
```

### 2. ngrok 외부 호스팅
```
1. ngrok 설치 https://ngrok.com/downloads/windows?tab=download
2. 실행 명령어 ngrok http 8051(자신의 포트번호)
3. 회원 가입 후 키 발급 확인
3-1. https://dashboard.ngrok.com/authtokens
4. 키 인증
4-1. ngrok config add-authtoken 32DAhV31Wq2vLJIr5WKWQ9vyN8v_2s9tVHTeD1WdCK23oVjFa
5. ngrok http 8080(자신의 포트번호) 외부 호스팅 2시간 무료
```

### 3. PPT 공유
```
노션 참고
```

### 4. model.fuse
[model.fuse](https://docs.ultralytics.com/reference/engine/model/#ultralytics.engine.model.Model.fuse)

---

### 5. YOLOE
[YOLOE](https://docs.ultralytics.com/ko/models/yoloe/)

---

### 6. OpenVINO
[OpenVINO](https://docs.ultralytics.com/ko/guides/optimizing-openvino-latency-vs-throughput-modes/)

---

### 7. Streamlit
[Streamlit](https://docs.ultralytics.com/ko/guides/streamlit-live-inference/)

---

### 8. Training
[Training](https://docs.ultralytics.com/yolov5/tutorials/tips_for_best_training_results/)

---

### 9. Line, MultiThread 관련 Ultralytics 공식 문서 자료
[Ultralytics](https://docs.ultralytics.com/ko/modes/track/#faq)

---

### 10. TensorRT 관련 Ultralytics 공식 문서 자료
[Ultralytics TensorRT](https://docs.ultralytics.com/ko/integrations/tensorrt/)

---

### 11. Miro
[Miro](https://miro.com/app/dashboard/)

---
