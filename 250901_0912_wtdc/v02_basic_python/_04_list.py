# 4. 값 변경과 리스트 조작

colors = ["red", "green", "blue"]

# 인덱싱
# print(colors[0]) # red
# print(colors[1]) # green
# print(colors[2]) # blue
# print(colors[-1]) # blue

# 슬라이싱
# print(colors[0:2]) # ['red', 'green']
# print(colors[0:3]) # ['red', 'green', 'blue']

# 값 변경
# print(colors) # ['red', 'green', 'blue']
# colors[-1] = "black"
# print(colors) # ['red', 'green', 'black']

# 값 추가
# colors.append("pink")
# print(colors) # ['red', 'green', 'blue', 'pink']

# 값 추가2
# colors.insert(0, "white")
# print(colors) # ['white', 'red', 'green', 'blue', 'pink']

# 값 제거
# colors.remove("white")
# print(colors) # ['red', 'green', 'blue', 'pink']

numbers = [5, 9, 1, 2, 7]

# 리스트 정렬
# numbers.sort() # 오름차순
# print(numbers) # [1, 2, 5, 7, 9]

numbers.sort(reverse=True) # 내림차순
# print(numbers) # [9, 7, 5, 2, 1]

numbers.reverse() # 역순
# print(numbers) # [7, 2, 1, 9, 5]

# 리스트 요소 포함 여부 확인
print(1 in numbers) # True
print(100 in numbers) # False