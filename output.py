def print_matrix(matrix, matrix_name):
    """Печатает матрицу в табличном виде."""
    print(f"\nМатрица {matrix_name}:")
    for row in matrix:
        print(" ".join(f"{value:5}" for value in row))


def print_result(columns, matrix_name):
    """Печатает номера подходящих столбцов или сообщение об их отсутствии."""
    if columns:
        numbers = ", ".join(map(str, columns))
        print(
            f"Матрица {matrix_name}: подходящие номера столбцов: {numbers}."
        )
    else:
        print(
            f"Матрица {matrix_name}: нет столбцов, "
            "в которых все элементы кратны 5 или 7."
        )
