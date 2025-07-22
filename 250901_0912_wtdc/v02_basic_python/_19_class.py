# 1. 클래스 : 제품의 설계도
# 2. 객체 : 설계도로 만든 제품
# 3. 속성 : 클래스 안의 변수
# 4. 생성자 : 객체를 만들 때 실행되는 함수
# 5. 메서드 : 클래스 안의 함수
# 6. 인스턴스 : 메모리에 살아있는 객체

# 객체 > 인스턴스 : 인스턴스는 객체 안에 포함되어 있음

# 클래스 정의
# class 클래스이름:
class World:
    # 생성자
    def __init__(self, name):
        # 속성
        self.name = name
    # 메서드
    def hello(self):
        print(self.name)


# 객체 생성
asia = World("korea")

# 메서드 호출
asia.hello()
   