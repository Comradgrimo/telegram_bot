import random
from datetime import datetime

from main import bot
from pascer_proxy import parser

while True:
    try:
        f = open('telegram_bot/ip_port.txt', 'r')
        l = [line.strip() for line in f]
        f.close()
        i = len(l)
        next_i = random.randint(0, i-1)
        proxy = l[next_i]
        bot(proxy)

    except Exception as e:
        print(f"Ошибка, время {datetime.now()}\n {e}")
        continue

