import random
import time
import os
import sys

# Слова для вида
words = [
    "ACCESSING MAINFRAME...",
    "BYPASSING FIREWALL...",
    "DECRYPTING RSA-4096...",
    "INJECTING PAYLOAD...",
    "CONNECTING TO 192.168.1.1...",
    "DOWNLOADING DATABASE...",
    "HACKING PENTAGON...",
    "TRACE BLOCKED",
    "PROXY CHAIN: 7 COUNTRIES",
    "SATELLITE UPLINK ESTABLISHED",
    "PASSWORD CRACKED: ********",
    "ROOT ACCESS OBTAINED",
    "ACCESS DENIED",
    "FIREWALL DETECTED",
    "ENCRYPTING DATA...",
]

# ASCII-череп
skull = r"""
        ______
     .-"      "-.
    /            \
   |              |     я сделала фейковый бенто
   |,  .-.  .-.  ,|
   | )(_o/  \o_)( |
   |/     /\     \|
   (_     ^^     _)
    \__|IIIIII|__/      pizda.
     | \IIIIII/ |
     \          /
      `--------`
"""

def random_line():
    if random.random() < 0.3:
        return random.choice(words)
    else:
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?"
        length = random.randint(20, 60)
        return "".join(random.choice(chars) for _ in range(length))

def progress_bar():
    """Рисует фейковый прогресс-бар."""
    print("\033[92m") # красный
    for i in range(0, 101, 2):
        bar = "█" * (i // 2) + "░" * (50 - i // 2)
        # Меняем цвет: до 50% зелёный, до 80% жёлтый, дальше красный
        if i < 50:
            color = "\033[92m"
        elif i < 80:
            color = "\033[93m"
        else:
            color = "\033[91m"
        sys.stdout.write(f"\r{color}[{bar}] {i}%")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\033[0m")

def main():
    os.system("clear")
    print("\033[92m")

    try:
        # Фаза 1: бегущие строки
        for _ in range(60):
            print(random_line())
            time.sleep(0.03)

        # Фаза 2: красная ошибка
        print("\033[91m")
        print("!!! ACCESS DENIED !!!")
        print("!!! TRACE DETECTED !!!")
        print("\033[92m")
        time.sleep(1)

        # Фаза 3: прогресс-бар
        progress_bar()
        time.sleep(0.5)

        # Фаза 4: успех
        print("\033[92m")
        print("ACCESS GRANTED")
        print("ROOT ACCESS OBTAINED")
        time.sleep(0.5)

    except KeyboardInterrupt:
        pass

    # Фаза 5: финальный череп
    os.system("clear")
    print("\033[91m")  # красный
    print(skull)
    print("\033[92m")
    print(">>> ВЗЛОМ ЗАВЕРШЁН. ПЕНТАГОН В ТВОИХ РУКАХ. <<<")
    print("\033[0m")

if __name__ == "__main__":
    main()
