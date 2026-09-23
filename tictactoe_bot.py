import random

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_win(player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw():
    return " " not in board

def get_move(player):
    while True:
        try:
            move = int(input(f"Игрок {player}, ваш ход (1-9): "))
        except ValueError:
            print("Введите число от 1 до 9!")
            continue
        if move < 1 or move > 9:
            print("Число должно быть от 1 до 9!")
            continue
        index = move - 1
        if board[index] != " ":
            print("Эта клетка уже занята!")
            continue
        return index

def computer_move():
    """Компьютер ходит в случайную свободную клетку."""
    empty = [i for i in range(9) if board[i] == " "]
    index = random.choice(empty)
    print(f"Компьютер ходит в клетку {index + 1}")
    return index

def main():
    print("Крестики-нолики против компьютера!")
    print("Ты — X, компьютер — O.")
    print("Клетки: 1-9 (слева направо, сверху вниз).")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    player = "X"

    while True:
        print_board()

        if player == "X":
            index = get_move(player)
        else:
            index = computer_move()

        board[index] = player

        if check_win(player):
            print_board()
            if player == "X":
                print("🎉 Ты победил!")
            else:
                print("💀 Компьютер победил!")
            break

        if is_draw():
            print_board()
            print("🤝 Ничья!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    main()
