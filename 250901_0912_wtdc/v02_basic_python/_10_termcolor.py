# pip install termcolor

from termcolor import colored

# 1. 기본 색상 출력
# print(colored("Hello", "red"))
# print(colored("GOOD", "blue"))
# print(colored("BYE", "yellow"))

# 2. 배경색 지정
# print(colored("World", "black", "on_yellow"))

# 3. 스타일 지정
print(colored("Hello, my name is Tom", "green"))
print(colored("Hello, my name is Tom", "green", attrs=["bold"]))
