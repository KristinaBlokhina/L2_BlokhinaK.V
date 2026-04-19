def get_negatives_1(lst):
    """Варіант 1: без генератора списку (цикл for)"""
    negatives = []
    for num in lst:
        if num < 0:
            negatives.append(num)
    return negatives

def get_negatives_2(lst):
    """Варіант 2: з генератором списку"""
    return [num for num in lst if num < 0]


print("Введіть числа через пробіл:")
user_input = input().strip()


try:
    a = [int(x) for x in user_input.split()]
    
    if not a:
        print("Список порожній!")
    else:
        print("\nВихідний список:", a)
        print("Від'ємні (варіант 1):", get_negatives_1(a))
        print("Від'ємні (варіант 2):", get_negatives_2(a))
        
except ValueError:
    print("Помилка: введіть тільки цілі числа, розділені пробілами!")