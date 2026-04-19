def remove_value_1(lst, n):
    """Варіант 1: без генератора списку"""
    new_lst = []
    for val in lst:
        if val != n:
            new_lst.append(val)
    return new_lst

def remove_value_2(lst, n):
    """Варіант 2: з генератором списку"""
    return [val for val in lst if val != n]


print("Введіть числа списку через пробіл:")
user_input = input().strip()

try:
    data = [int(x) for x in user_input.split()]
    
    if not data:
        print("Список порожній!")
    else:
        print(f"\nОригінальний список: {data}")
        
        n = int(input("Введіть число, яке потрібно видалити: "))
        
        print(f"\nПісля видалення {n} (варіант 1): {remove_value_1(data, n)}")
        print(f"Після видалення {n} (варіант 2): {remove_value_2(data, n)}")
        
except ValueError:
    print("Помилка: введіть тільки цілі числа, розділені пробілами!")