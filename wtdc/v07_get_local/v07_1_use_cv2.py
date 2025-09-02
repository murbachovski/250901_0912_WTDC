import cv2
import os
from datetime import datetime

# 1. 저장 디렉토리 설정
save_dir = "./captured_images"
os.makedirs(save_dir, exist_ok=True)

# 2. 카메라 연결
cap = cv2.VideoCapture(0)

# 3. 프레임 처리
if not cap.isOpened():
    raise RuntimeError("카메라 연결 안됨")

print("카메라 연결 됐습니다.")
success, frame = cap.read()
if success:
    print("OPEN")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(save_dir, f"result_{timestamp}.jpg")
    
    cv2.imwrite(file_path, frame)
    print(f"사진이 저장 됐습니다. {file_path}")
else:
    print("프레임 읽기 실패")
    
# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()