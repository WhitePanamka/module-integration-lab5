# Модуль обработки матриц.
# Ответственный: Ильин Владислав ИСП-43-23

def is_valid_column(column):
    """
    Возвращает True, если каждый элемент столбца кратен 5 или 7.
    Столбец передаётся в функцию целиком в виде списка.
    """
    return all(value % 5 == 0 or value % 7 == 0 for value in column)


def find_valid_columns(matrix):
    """Возвращает номера (с 1) столбцов, удовлетворяющих условию."""
    if not matrix or not matrix[0]:
        return []

    valid_columns = []
    column_count = len(matrix[0])

    for column_index in range(column_count):
        column = [row[column_index] for row in matrix]
        if is_valid_column(column):
            valid_columns.append(column_index + 1)

    return valid_columns
