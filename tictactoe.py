# Игровое поле 3x3. Пустые клетки обозначены пробелами.
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def print_board():
    """Рисует игровое поле."""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_win(player):
    """Проверяет, выиграл ли игрок."""
    # Все возможные выигрышные комбинации (индексы клеток)
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # строки
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # столбцы
        (0, 4, 8), (2, 4, 6)              # диагонали
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw():
    """Проверяет, закончилась ли игра вничью."""
    return " " not in board

def get_move(player):
    """Спрашивает у игрока ход и проверяет его."""
    while True:
        try:
            move = int(input(f"Игрок {player}, ваш ход (1-9): "))
        except ValueError:
            print("Введите число от 1 до 9!")
            continue

        if move < 1 or move > 9:
            print("Число должно быть от 1 до 9!")
            continue

        index = move - 1  # Превращаем 1-9 в индексы 0-8
        if board[index] != " ":
            print("Эта клетка уже занята!")
            continue

        return index

def main():
    print("Крестики-нолики!")
    print("Клетки пронумерованы от 1 до 9 (слева направо, сверху вниз):")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    
    player = "X"
    
    while True:
        print_board()
        index = get_move(player)
        board[index] = player
        
        if check_win(player):
            print_board()
            print(f"🎉 Игрок {player} победил!")
            break
        
        if is_draw():
            print_board()
            print("🤝 Ничья!")
            break
        
        # Меняем игрока
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    main()
