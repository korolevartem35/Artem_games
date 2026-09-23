player = {
    "hp": 100,
    "max_hp": 100,
    "aura": 5,
    "gold": 0,
    "sword": False,
    "potion": 2,
    "visited": set(),
    "game_over": False
}

def show_status():
    print(f"\n❤️ HP: {player['hp']}/{player['max_hp']} | "
          f"💰 Золото: {player['gold']} | "
          f"⚔️ Меч: {'да' if player['sword'] else 'нет'} | "
          f"аптека: {player['potion']}"
          f"аура: {player['aura']}")
def use_potion():
    if player["potion"] > 0:
        player["potion"] -= 1
        player["hp"] = min(player["max_hp"], player["hp"] + 30)
        print("на аптечку! +30 HP.")
    else:
        print("аптека закрыта")

def main_menu():
    show_status()
    print("\n📍 Ты в деревне. Куда идти?")
    print("1 — Лес рук")
    print("2 — Пещера пидоров")
    print("3 — Древний храм")
    print("4 — похавать")
    print("5 — нахуй")

    choice = input("Выбор: ")

    if choice == "1":
        forest()
    elif choice == "2":
        cave()
    elif choice == "3":
        temple()
    elif choice == "4":
        use_potion()
    elif choice == "5":
        player["game_over"] = True
        print("Игра окончена.")
    else:
        print("Неверный выбор.")

def forest():
    if "forest" not in player["visited"]:
        player["visited"].add("forest")
        print("\n🌲 Ты в лесу рук. Тут можно найти бабки.")
        player["gold"] += 30
        print("+30 бабла!")
    else:
        print("\n🌲 Ты снова в лесу рук. Тут уже пусто.")

    choice = input("Идти вглубь или вернуться? (вглубь/назад): ").lower()
    if choice == "вглубь":
        print("Ты находишь сундук!")
        player["gold"] += 50
        player["aura"] += 45
        print("+50 бабла.аура повышена!")
    else:
        print("Ты возвращаешься в деревню.")

def cave():
    print("\n🕳️ Ты в пещере пидоров.")
    if not player["sword"]:
        print("Ты находишь меч!аура повышена")
        player["aura"] += 20
        player["sword"] = True
    else:
        print("Тут пусто.")

    print("Из темноты выходит пидр!")
    if player["sword"]:
        print("Ты побеждаешь пидора мечом!")
        player["gold"] += 20
        player["aura"] += 20
        print("+20 бабла.аура повышена")
    else:
        print("пидр бьёт тебя.аура опустилась,да и как ты такое мог допустить")
        player["hp"] -= 30
        print("-30 HP.")
        player["aura"] -= 10

def temple():
    print("\n🏛️ Ты в древнем храме. Тут дракон!")
    if player["hp"] < 50:
        print("Ты слишком ничтожен. Дракон убивает тебя.")
        player["hp"] = 0
        return

    print("Ты сражаешься с драконом!")
    player["hp"] -= 40
    print("-40 HP.")
    player["gold"] += 100
    player["aura"] += 9999909
    print("🏆 Ты победил дракона! +100 золота. ты стал супер крут и съебался")
    player["game_over"] = True

print("=== ПРИКЛЮЧЕНИЕ ===")
while not player["game_over"] and player["hp"] > 0:
    main_menu()

if player["hp"] <= 0:
    print("💀 Ты погиб.ты слишкол слабый. Игра окончена.")
else:
    print("\n🏆 все,я съебываю нахуй.Ты прошёл игру.")
    show_status()

player["visited"] = set()
player["visited"].add("forest")
if "forest" in player["visited"]:
    print("Ты уже был тут")
