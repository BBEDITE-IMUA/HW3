def IsSymetric(A):
    # Создаём вложенный цикл:
    for i in range(n):
        for j in range(n):
            # Проверяем, если противоположные элементы не равны друг другу то выводим False и завершаем функцию:
            if A[i][j] != A[j][i]:
                return False
    # Если не было ошибок то выводим True:
    return True