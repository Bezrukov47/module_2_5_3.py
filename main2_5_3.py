# ФУНКЦИИ В PYTHON
def get_matrix(n, m, value): # Объявил функцию
    matrix = [] # пустой список
    for i in range(n): # Внешний цикл для n повторов
        matrix.append([]) # Пустой список для каждой строки

        for _ in range(m): # Внутренний цикл для m столбцов
            matrix[i].append(value) # Добавляем значение в текущую строку по индексу
    return matrix # Возвращение созданной матрицы

# Пример результата выполнения функции с заданными величинами
result1 = get_matrix(6, 7, 77)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(5, 8, 56)
print(result1)
print(result2)
print(result3)
