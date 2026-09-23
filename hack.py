import random
import time
import os

# Список «хакерских» слов для вида
words = [
    "ACCESSING MAINFRAME...",
    "BYPASSING FIREWALL...",
    "DECRYPTING RSA-4096...",
    "INJECTING PAYLOAD...",
    "CONNECTING TO 192.168.1.1...",
    "DOWNLOADING DATABASE...",
    "HACKING PENTAGON...",
    "ACCESS GRANTED",
    "TRACE BLOCKED",
    "PROXY CHAIN: 7 COUNTRIES",
    "SATELLITE UPLINK ESTABLISHED",
    "PASSWORD CRACKED: ********",
    "ROOT ACCESS OBTAINED",
]

def random_line():
    """Генерирует строку из случайных символов или хакерских слов."""
    if random.random() < 0.3:  # 30% шанс, что будет слово
        return random.choice(words)
    else:
        # Случайные символы (буквы, цифры, знаки)
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?"
        length = random.randint(20, 60)
        return "".join(random.choice(chars) for _ in range(length))

def main():
    os.system("clear")  # Очистить экран
    
    print("\033[92m")  # Включить зелёный цвет
    
    try:
        while True:
            line = random_line()
            print(line)
            time.sleep(0.05)  # Пауза 0.05 сек между строками
    except KeyboardInterrupt:
        print("\033[0m")  # Вернуть обычный цвет
        print("\n>>> ВЗЛОМ ЗАВЕРШЁН. ПЕНТАГОН В ТВОИХ РУКАХ.тоби пизда <<<")

if __name__ == "__main__":
    main()
