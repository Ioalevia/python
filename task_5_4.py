src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [num for prev_num, num in zip(src[0:], src[1:]) if num > prev_num]
print(result)