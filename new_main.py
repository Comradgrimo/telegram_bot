import random
from datetime import datetime

from main import bot
from pascer_proxy import parser

while True:
    try:
        p = parser()
        i = len(p)
        next_i = random.randint(0, i-1)
        proxy = p[next_i]

        bot(proxy, '1080')
    except Exception as e:
        print(f"Ошибка, время {datetime.now()}\n {e}")
        continue

