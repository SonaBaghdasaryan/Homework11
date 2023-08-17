#Добавьте ко всем задачам с семинара строки документации и методы вывода
# информации на печать.
from builtins import list, len, property, str, isinstance, range, all, print, sum


# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц.



class Matrix:


    def __init__(self, list_of_lists: list[list[int]]):
        self.list_of_lists = list_of_lists

    def __str__(self):
        result = ''
        for row in self.list_of_lists:
            for elem in row:
                result += ''.join(f'{elem}\t')
            result += ''.join('\n')
        return result

    def __eq__(self, other):
        return True if self.list_of_lists == other.list_of_lists else False

    def __add__(self, other):
        result = []
        row = []
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[0])):
                row.append(self.list_of_lists[i][j] + other.list_of_lists[i][j])
            result.append(row)
            row = []
        return Matrix(result)

    def __mul__(self, other):
        m = len(self.list_of_lists)
        n = len(other.list_of_lists)
        k = len(other.list_of_lists[0])
        result = [[0 for _ in range(k)] for _ in range(m)]
        for i in range(m):
            for j in range(k):
                result[i][j] = sum(self.list_of_lists[i][k] * other.list_of_lists[k][j] for k in range(n))
        return Matrix(result)


if __name__ == '__main__':
    matrix_1 = Matrix([[4, 2, 8], [6, 8, 2], [2, 4, 6]])
    matrix_2 = Matrix([[3, 5, 7], [1, 5, 9], [5, 1, 7]])
    print(matrix_1, matrix_2, sep='\n\n')
    print(matrix_1 == matrix_2)
    matrix_sum = matrix_1 + matrix_2
    print(matrix_sum)
    matrix_mul = matrix_1 * matrix_2
    print(matrix_mul)
    if matrix_1 == matrix_2:
        print('True')
    else:
        print('False')