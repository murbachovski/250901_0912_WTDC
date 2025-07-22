# pyfiglet + termcolor

import pyfiglet
from termcolor import colored

# 1. 폰트 입히기
py_sentence = pyfiglet.figlet_format("*")

# 2. 색상 입히기
color_py_sentence = colored(py_sentence, "red")

# 3. 출력
print(color_py_sentence)
