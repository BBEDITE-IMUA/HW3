# Задаём список с клавиатуры:
matrix = [int(_) for _ in input().split()]
result = 0
# Проходим по элементам списка:
for i in range(len(matrix)):
    for j in range(i + 1, len(matrix)):
        # Если элемент совпалает с другим элементом, то в значение добавляется +1:
        if matrix[i] == matrix[j]:
            result = result + 1
print(result)