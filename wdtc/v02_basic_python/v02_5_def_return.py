# pyfigel + termcolor 를 적용한 함수!
import pyfiglet
from termcolor import colored

# 함수 정의
def decorate_text(text : str, color : str):
    '''
    함수 설명:
    1. 폰트 적용
    2. 색상 적용
    3. 출력
    
    매개 변수:
    1. text : str
    2. color : str
    '''
    py_sentence = pyfiglet.figlet_format(text)
    decorate_sentence = colored(py_sentence, color)
    # print(decorate_sentence)
    return decorate_sentence
    
# 출력1
print(decorate_text("Hello", "red"))

# 출력2
good_sentence = decorate_text("GOOD", "yellow")
print(good_sentence)

