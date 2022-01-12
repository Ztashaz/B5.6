def greet():
    print("--------------------")
    print("  Добро пожаловать  ")
    print("       в игру       ")
    print("  крестики-нолики   ")
    print("--------------------")
    print("    Правила игры:   ")
    print(" укажите координаты ")
    print("   в формате х, у   ")
    print("  (номер строки и   ")
    print("   номер столбца)   ")
    print("--------------------")
    
def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print(" _________________")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print(" _________________")
    print()
    
def ask_player():
    
    while True:
        dots = input("Введите координаты x, y:").split()
        
        if len(dots) != 2:
            print("Введите 2 координаты")
            continue
        
        x, y = dots
        
        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue
        
        x, y = int(x), int(y)
        
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Координаты вне диапазона")
            continue    
                
        if field[x][y] != " ":
            print("Клетка занята!")
            continue
        
        return x, y

def check_combs():
    win_dots = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
               ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
               ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)))
    for dot in win_dots:
        symbols = []
        for c in dot:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл крестик X!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл нолик 0!")
            return True
        
    return False    

greet()

field = [[" "] * 3 for i in range(3) ]

count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")
    x, y = ask_player()
    
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    
    if check_combs():  
        show()
        break
    if count == 9:
        print(" Ничья!")
        show()
        break
    
print("--------------------")
print("     До свидания    ")
print("--------------------")