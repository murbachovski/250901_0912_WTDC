# pyfiglet => 함수화 => lambda

import pyfiglet

def good_sentence(sentence):
    '''
    함수 설명:
        입력된 문자열을 pyfiglet 형식으로 출력합니다.
    매개변수:
        sentence (str): 출력할 문자열
    '''
    py_sentence = pyfiglet.figlet_format(sentence)
    print(py_sentence)
    
