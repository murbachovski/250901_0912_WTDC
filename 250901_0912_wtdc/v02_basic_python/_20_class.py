# 클래스 정의
class Animal:
    '''
    이건 동물 클래스야
    '''
    # 생성자
    def __init__(self, name, age):
        # 속성
        self.name = name
        self.age = age
    # 메서드
    def hello(self):
        print(f"안녕하세요. 저는 {self.name} 입니다. 그리고 {self.age}살이야.")

# 객체 생성
dog = Animal("뽀삐", 99)

# 메서드 호출
dog.hello()

# a = [1, 2, 3]
# a.append()