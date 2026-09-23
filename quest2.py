# Состояние игрока
player = {
    "hp": 100,
    "gold": 0,
    "sword": False,
    "potion": 1
}

def show_status():
    print(f"\n❤️ HP: {player['hp']} | 💰 Золото: {player['gold']} | ⚔️ Меч: {'да' if player['sword'] else 'нет'} | 🧪 Зелье: {player['potion']}")

def use_potion():
    if player["potion"] > 0:
        player["potion"] -= 1
        player["hp"] = min(100, player["hp"] + 30)
        print("Ты выпил зелье. +30 HP.")
    else:
        print("Зелий больше нет!")

def fight_goblin():
    print("\nНа тебя напал гоблин!")
    if player["sword"]:
        print("Ты побеждаешь гоблина мечом!")
        player["gold"] += 20
        print("+20 золота.")
    else:
        print("У тебя нет меча. Гоблин бьёт тебя.")
        player["hp"] -= 30
        print("-30 HP.")

def forest():
    print("\nТы в тёмном лесу.")
    choice = input("Идти вперёд или вернуться? (вперёд/назад): ").lower()

    if choice == "вперёд":
        print("Ты находишь сундук.")
        player["gold"] += 50
        print("+50 золота!")
        print("🏆 Победа! Ты разбогател.")
    else:
        village()

def cave():
    print("\nТы в пещере.")
    if not player["sword"]:
        print("Ты находишь меч!")
        player["sword"] = True
    else:
        print("Тут пусто.")
    
    print("Из темноты выходит гоблин!")
    fight_goblin()

    if player["hp"] <= 0:
        print("💀 Ты погиб.")
        return
    
    choice = input("Идти дальше или вернуться? (дальше/назад): ").lower()
    if choice == "дальше":
        forest()
    else:
        village()

def village():
    show_status()
    print("\nТы в деревне. Куда идти?")
    print("1 — В лес")
    print("2 — В пещеру")
    print("3 — Выпить зелье")
    print("4 — Выйти из игры")

    choice = input("Выбор: ")

    if choice == "1":
        forest()
    elif choice == "2":
        cave()
    elif choice == "3":
        use_potion()
        village()
    elif choice == "4":
        print("Игра окончена.")
    else:
        print("Неверный выбор.")
        village()

# Запуск
print("=== ПРИКЛЮЧЕНИЕ ===")
village()
