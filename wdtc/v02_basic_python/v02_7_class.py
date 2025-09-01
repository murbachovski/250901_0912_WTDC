# 클래스 정의
class Animal:
    # 생성자
    def __init__(self, name, age):
        # 속성
        self.name = name
        self.age = age
    # 메서드
    def introduce(self):
        print(f"안녕하세요. 저는 {self.name} 입니다. 그리고 {self.age}살입니다.")

# 객체 생성
dog = Animal("뽀삐", 99)

# 메서드 호출
dog.introduce()
# 안녕하세요. 저는 뽀삐 입니다. 그리고 99살입니다.