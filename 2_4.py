def insert_before_index(lst, index, value):
    """Вставляє value перед елементом з індексом index (без insert)"""
    if index < 0 or index > len(lst):
        raise IndexError("Індекс поза межами списку")
    # Розбиваємо список на дві частини та з'єднуємо з новим елементом
    return lst[:index] + [value] + lst[index:]

# Введення даних від користувача
print("Введіть числа списку через пробіл:")
user_input = input().strip()

try:

    my_list = [int(x) for x in user_input.split()]
    
    if not my_list:
        print("Список порожній!")
    else:
        print(f"\nОригінальний список: {my_list}")
        
        idx = int(input(f"Введіть індекс (від 0 до {len(my_list)}): "))
        
        val = int(input("Введіть значення для вставки: "))
        
        if 0 <= idx <= len(my_list):
            new_list = insert_before_index(my_list, idx, val)
            print(f"\nПісля вставки {val} перед індексом {idx}: {new_list}")
        else:
            print(f"Помилка: індекс має бути від 0 до {len(my_list)}")
        
except ValueError:
    print("Помилка: введіть тільки цілі числа!")
except IndexError as e:
    print(f"Помилка: {e}")