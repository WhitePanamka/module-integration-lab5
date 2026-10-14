from input_module import input_matrix
from processing import find_valid_columns
from output import print_matrix, print_result


def main():
    print("Лабораторная работа № 5")
    print("Вариант 1. Поиск столбцов, содержащих только числа, кратные 5 или 7.")
    print()

    matrix_a = input_matrix("A")
    matrix_b = input_matrix("B")

    print_matrix(matrix_a, "A")
    print_matrix(matrix_b, "B")

    columns_a = find_valid_columns(matrix_a)
    columns_b = find_valid_columns(matrix_b)

    print("\nРезультаты обработки:")
    print_result(columns_a, "A")
    print_result(columns_b, "B")


if __name__ == "__main__":
    main()
