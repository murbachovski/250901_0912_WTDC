# 7. for문 활용

mixed = [1, "hello", 3.14, True]

# 리스트 반복문
# for i in mixed:
#     print(i)
# 1
# hello
# 3.14
# True

for index, value in enumerate(mixed):
    # print(index)
    # print(value)
    print(f"index : {index}, value : {value}")
# index : 0, value : 1
# index : 1, value : hello
# index : 2, value : 3.14
# index : 3, value : True
