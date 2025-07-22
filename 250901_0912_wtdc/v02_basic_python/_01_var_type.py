# 1. 기본적인 변수 타입
    # - 변수들이 이렇게 생겼군!!

# 변수 목록
# 1
x = 10 # 정수형
# 2
y = 3.14 # 실수형
# 3
name = "Python" # 문자열
# 4
is_python_fun = True # 불리언
# 5
colors = ["red", "green", "blue"] # 리스트
# 6
coords = (10, 20) # 튜플
# 7
perosn = {"name" : "Tom", "age" : 30} # 딕셔너리
# 8
unique_values = {1, 2, 3} # 집합
# 9
nothing = None # NoneType

# 출력
# print("x의 값 : ", x) # x의 값 :  10
# print(y) # 3.14
# print(perosn) # {'name': 'Tom', 'age': 30}

# 타입 출력
# print(type(x))# <class 'int'>

# 주석 단축키 : Ctrl + /

# 변수가 특정 유형인지 확인
print(isinstance(name, str)) # True
print(isinstance(name, int)) # False