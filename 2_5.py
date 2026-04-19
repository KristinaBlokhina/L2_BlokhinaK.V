# Початковий словник
groups = {
    "Група1": {"кількість": 20, "староста": "Петренко П.П."},
    "Група2": {"кількість": 25, "староста": "Іваненко І.І."},
    "Група3": {"кількість": 18, "староста": "Сидоренко С.С."},
}

def show_menu():
    print("\n--- Меню ---")
    print("1. Кількість студентів у групі")
    print("2. ПІБ старости групи")
    print("3. Групи з кількістю ≤ заданого")
    print("4. Групи з кількістю ≥ заданого")
    print("5. Змінити кількість студентів")
    print("6. Змінити ПІБ старости")
    print("7. Додати нову групу")
    print("8. Видалити групу")
    print("9. Множина ПІБ старост зазначених груп")
    print("10. Вихід")

def get_group(groups_dict, name):
    return groups_dict.get(name)

# Головний цикл
while True:
    show_menu()
    choice = input("Ваш вибір: ")
    
    if choice == "1":
        grp = input("Назва групи: ")
        if grp in groups:
            print(f"Кількість студентів: {groups[grp]['кількість']}")
        else:
            print("Групу не знайдено")
    
    elif choice == "2":
        grp = input("Назва групи: ")
        if grp in groups:
            print(f"Староста: {groups[grp]['староста']}")
        else:
            print("Групу не знайдено")
    
    elif choice == "3":
        limit = int(input("Максимальна кількість: "))
        result = tuple(grp for grp, data in groups.items() if data["кількість"] <= limit)
        print("Групи:", result)
    
    elif choice == "4":
        limit = int(input("Мінімальна кількість: "))
        result = tuple(grp for grp, data in groups.items() if data["кількість"] >= limit)
        print("Групи:", result)
    
    elif choice == "5":
        grp = input("Назва групи: ")
        if grp in groups:
            new_count = int(input("Нова кількість: "))
            groups[grp]["кількість"] = new_count
            print("Оновлено")
        else:
            print("Групу не знайдено")
    
    elif choice == "6":
        grp = input("Назва групи: ")
        if grp in groups:
            new_head = input("Нове ПІБ старости: ")
            groups[grp]["староста"] = new_head
            print("Оновлено")
        else:
            print("Групу не знайдено")
    
    elif choice == "7":
        grp = input("Назва нової групи: ")
        if grp in groups:
            print("Така група вже існує")
        else:
            count = int(input("Кількість студентів: "))
            head = input("ПІБ старости: ")
            groups[grp] = {"кількість": count, "староста": head}
            print("Групу додано")
    
    elif choice == "8":
        grp = input("Назва групи для видалення: ")
        if grp in groups:
            del groups[grp]
            print("Видалено")
        else:
            print("Групу не знайдено")
    
    elif choice == "9":
        group_names = input("Введіть назви груп через пробіл: ").split()
        # Множина ПІБ старост для вказаних груп
        result_set = {groups[g]["староста"] for g in group_names if g in groups}
        print("Множина ПІБ старост:", result_set)
    
    elif choice == "10":
        print("Вихід")
        break
    
    else:
        print("Некоректний вибір")