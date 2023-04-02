# Создаём временный список, который мы будем добавлять в конец постоянного списка:
a = int(input())
matrix = [1]
timeMatrix = []
while (len(matrix) < a):
# Инверсируем список matrix и помещаем результат в timeMatrix:
    for i in range(len(matrix)):
        if matrix[i] == 0:
            b = 1
        else:
            b = 0
        timeMatrix.append(b)
    matrix += timeMatrix
# Очищаем временный список: 
    timeMatrix = []
# Выводим срез:
print(*matrix[0 : a])
