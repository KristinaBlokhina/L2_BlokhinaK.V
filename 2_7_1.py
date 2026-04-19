def transpose(matrix):
    """Транспонує список списків (матрицю)"""
    if not matrix:
        return []
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        new_row = [matrix[i][j] for i in range(len(matrix))]
        result.append(new_row)
    return result

def input_matrix():
    """Функція для введення матриці з клавіатури"""
    print("Введіть кількість рядків матриці:")
    rows = int(input("Рядки: "))
    
    if rows == 0:
        return []
    
    print("Введіть кількість стовпців матриці:")
    cols = int(input("Стовпці: "))
    
    matrix = []
    print(f"\nВведіть {rows} рядків по {cols} чисел у кожному:")
    print("(Числа вводьте через пробіл)")
    
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Рядок {i+1}: ").strip().split()
                if len(row_input) != cols:
                    print(f"Помилка: потрібно {cols} чисел! Спробуйте ще раз.")
                    continue
                row = list(map(float, row_input))
                matrix.append(row)
                break
            except ValueError:
                print("Помилка: введіть коректні числа!")
    
    return matrix

def print_matrix(matrix, name="Матриця"):
    """Функція для виведення матриці"""
    print(f"\n{name}:")
    for row in matrix:
        print(row)

if __name__ == "__main__":
    print("="*50)
    print("ТРАНСПОНУВАННЯ МАТРИЦІ")
    print("="*50)
    
    # Введення матриці
    matrix = input_matrix()
    
    if not matrix:
        print("Порожня матриця")
    else:
        print_matrix(matrix, "Вхідна матриця")
        
        # Транспонування
        transposed = transpose(matrix)
        print_matrix(transposed, "Транспонована матриця")
