class Matrix:
    def __init__(self, rows, columns):
        # Ініціалізація матриці нулями
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def add_element(self, row, col, value):
        # Додавання елемента у вказану позицію
        if 0 <= row < self.rows and 0 <= col < self.columns:
            self.data[row][col] = value
        else:
            raise IndexError("Row or column out of bounds")

    def sum_of_rows(self):
        # Обчислення суми кожного рядка та повернення списоку сум
        return [sum(row) for row in self.data]

    def transpose(self):
        # Створення нової транспонованої матриці
        transposed_matrix = Matrix(self.columns, self.rows)
        for row in range(self.rows):
            for col in range(self.columns):
                transposed_matrix.add_element(col, row, self.data[row][col])
        return transposed_matrix

    def multiply_by(self, other_matrix):
        # Перемноження двох матриць та повернення результату
        if self.columns != other_matrix.rows:
            raise ValueError("Incompatible matrices for multiplication")

        result_matrix = Matrix(self.rows, other_matrix.columns)
        for i in range(self.rows):
            for j in range(other_matrix.columns):
                for k in range(self.columns):
                    result_matrix.data[i][j] += self.data[i][k] * other_matrix.data[k][j]
        return result_matrix

    def is_symmetric(self):
        # Перевірка матриці на симетричність
        if self.rows != self.columns:
            return False
        
        for i in range(self.rows):
            for j in range(i, self.columns):
                if self.data[i][j] != self.data[j][i]:
                    return False
        return True

    def rotate_right(self):
        # Перевертання матриці на 90 градусів праворуч
        rotated_matrix = Matrix(self.columns, self.rows)
        for row in range(self.rows):
            for col in range(self.columns):
                rotated_matrix.add_element(col, self.rows - row - 1, self.data[row][col])
        self.data = rotated_matrix.data
        self.rows, self.columns = rotated_matrix.rows, rotated_matrix.columns

    def flatten(self):
        # Зведення матриці до єдиного списку
        flattened_list = []
        for row in self.data:
            flattened_list.extend(row)
        return flattened_list

    @staticmethod
    def from_list(list_of_lists):
        # Створення матриці зі списку списків
        rows = len(list_of_lists)
        columns = len(list_of_lists[0]) if rows > 0 else 0
        matrix = Matrix(rows, columns)
        matrix.data = list_of_lists
        return matrix

    def diagonal(self):
        # Виділення діагоналі квадратної матриці
        if self.rows != self.columns:
            raise ValueError("Matrix is not square")
        
        diagonal = [self.data[i][i] for i in range(self.rows)]
        return diagonal

matrix = Matrix(2, 3)
print(matrix.data)  

matrix.add_element(0, 2, 10)
print(matrix.data)  

print(matrix.sum_of_rows())  

transposed = matrix.transpose()
print(transposed.data)  

matrix1 = Matrix(2, 3)
matrix1.add_element(0, 0, 1)
matrix1.add_element(0, 1, 2)
matrix1.add_element(0, 2, 3)

matrix2 = Matrix(3, 2)
matrix2.add_element(0, 0, 1)
matrix2.add_element(1, 0, 2)
matrix2.add_element(2, 0, 3)

result = matrix1.multiply_by(matrix2)
print(result.data) 

matrix3 = Matrix(2, 2)
matrix3.add_element(0, 0, 1)
matrix3.add_element(0, 1, 2)
matrix3.add_element(1, 0, 3)
matrix3.add_element(1, 1, 4)
matrix3.rotate_right()
print(matrix3.data)  

matrix4 = Matrix(2, 2)
matrix4.add_element(0, 0, 1)
matrix4.add_element(0, 1, 2)
matrix4.add_element(1, 0, 3)
matrix4.add_element(1, 1, 4)
print(matrix4.flatten()) 

list_of_lists = [[1, 2], [3, 4]]
matrix5 = Matrix.from_list(list_of_lists)
print(matrix5.data)  

matrix6 = Matrix(3, 3)
matrix6.add_element(0, 0, 1)
matrix6.add_element(1, 1, 2)
matrix6.add_element(2, 2, 3)
print(matrix6.diagonal())  
