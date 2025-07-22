# figlet + termcolor => 함수

import pyfiglet
from termcolor import colored

# 1. text, color를 받는 함수 정의
def decorate_text(text, color):
    '''
        함수 설명 :
            1. 폰트 적용
            2. 색상 적용
            3. 출력
        매개 변수 :
            1. text
            2. color 
    '''
    py_sentence = pyfiglet.figlet_format(text)
    color_py_sentence = colored(py_sentence, color)
    print(color_py_sentence)
    
# 2. 출력
decorate_text()

# 3. 결과
# text = *GOOD*, color = 'yellow'
