import pyfiglet
from termcolor import colored

def decorated_text(text, color):
    py_sentence = pyfiglet.figlet_format(text)
    color_py_sentence = colored(py_sentence, color)
    
    return color_py_sentence

decorated_text("HELLO", "blue")

# 결과물 출력해주세요.
    # finish_text = decorated_text("HELLO", "blue")
    # print(finish_text) => 이 방식 선호
    # print(decorated_text("HELLO", "blue"))
# return을 사용하는 이유
    # 함수의 실행 결과(값)를 함수 밖으로 전달할 수 있습니다.
    # 반환된 값을 변수에 저장하거나, 다른 함수의 입력값으로 활용할 수 있습니다.
    # 함수의 재사용성과 확장성이 높아집니다(여러 곳에서 결과를 다양하게 활용 가능).
    # 함수 내부에서만 출력(print)하면 결과를 저장하거나 추가로 처리할 수 없습니다.