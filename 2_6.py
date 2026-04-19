def solve_catia_ivan():
    n = int(input("n = "))
    possible = set(range(1, n + 1))
    
    while True:
        line = input().strip()
        if line == "Все":
            break
        
        numbers = list(map(int, line.split()))
        answer = input().strip()
        
        query_set = set(numbers)
        
        # Якщо Катя питає рівно половину з можливих -> Іван каже "Ні"
        if len(query_set & possible) * 2 == len(possible):
            possible = possible - query_set
        else:
            inside = query_set & possible
            outside = possible - query_set
            
            if len(inside) > len(outside):
                if answer == "Так":
                    possible = inside
                else:
                    possible = outside
            elif len(outside) > len(inside):
                if answer == "Ні":
                    possible = outside
                else:
                    possible = inside
            else:  # рівно
                if answer == "Ні":
                    possible = outside
                else:
                    possible = inside
    
    # Виводимо результат
    if possible:
        print(" ".join(map(str, sorted(possible))))
    else:
        print("Немає можливих чисел")

# Головна функція
if __name__ == "__main__":
    solve_catia_ivan()
