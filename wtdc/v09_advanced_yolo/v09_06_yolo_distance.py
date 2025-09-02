from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("v09_advanced_yolo/input_distance.mp4")

# 2. 거리 계산 객체 생성
distance_calculator = solutions.DistanceCalculation(
    model="yolo11n.pt",
    show=True
)

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    results = distance_calculator(frame)
    # temp_distance = distance_calculator.process(frame)
    # temp2_distance = temp_distance.pixels_distance
    # print(temp2_distance)
    
    check_distance = distance_calculator.process(frame).pixels_distance
    print(check_distance)
    
    if check_distance >= 100:
        status = "Safe"
        color = (0, 0, 0)
    else:
        status = "Danger"
        color = (0, 0, 255)

    cv2.putText(
        frame,
        status,
        (400, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        2
    )
    
    cv2.imshow("Ultralytics Solutions", frame)
    cv2.waitKey(1)
    
# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()

# 영상에 거리에 따른 조건 정의 출력