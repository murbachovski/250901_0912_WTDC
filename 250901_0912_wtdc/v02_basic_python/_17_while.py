def meters_to_feet(meters):
    feet = meters * 3.28084 # 1미터는 약 3.28074피트
    
    return feet

while True:
    # 1. 사용자 입력 받기
    user_input = input("미터 값을 입력해주세요. : ")
    try:
        # 2. meters 변수 => float 타입 적용
        meters = float(user_input)
        # 3. feet 환산
        feet = meters_to_feet(meters)
        print(f"{meters}m는 {feet}ft 입니다.")
        # 4. 완료 되면 종료
        break
    except ValueError:
        print("숫자를 입력해주세요.")