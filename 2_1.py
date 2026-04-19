import random

def fill_list(n, a, b):
    """Повертає список із n випадкових цілих чисел у діапазоні [a, b]"""
    return [random.randint(a, b) for _ in range(n)]

# Приклад використання
n = int(input("Кількість елементів n: "))
a = int(input("Нижня межа a: "))
b = int(input("Верхня межа b: "))

result = fill_list(n, a, b)
print("Згенерований список:", result)