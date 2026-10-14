def input_matrix(matrix_name):
    """Ввод матрицы натуральных чисел размером от 1x1 до 10x10."""
    while True:
        try:
            rows = int(input(f"Введите количество строк матрицы {matrix_name} (1-10): "))
            cols = int(input(f"Введите количество столбцов матрицы {matrix_name} (1-10): "))
        except ValueError:
            print("Ошибка: размеры должны быть целыми числами.")
            continue

        if 1 <= rows <= 10 and 1 <= cols <= 10:
            break

        print("Ошибка: количество строк и столбцов должно быть от 1 до 10.")

    matrix = []
    print(f"Введите элементы матрицы {matrix_name}, по одной строке за раз.")

    for row_index in range(rows):
        while True:
            try:
                row = list(map(int, input(f"Строка {row_index + 1}: ").split()))
            except ValueError:
                print("Ошибка: вводите только целые числа.")
                continue

            if len(row) != cols:
                print(f"Ошибка: нужно ввести ровно {cols} чисел.")
                continue

            if any(value <= 0 for value in row):
                print("Ошибка: все элементы должны быть натуральными числами (больше нуля).")
                continue

            matrix.append(row)
            break

    return matrix
