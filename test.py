#
# for i in 'hello':
#     if i=='w':
#         print(i)
#         break
# else:
#     print("fffffe")
# import psutil
# for proc in psutil.process_iter():
#     name = proc.name()
#     print(name)
#     if name == "anyDesk.exe":
#         print("11111111")
import subprocess
if subprocess.call('python C:/Users/ReshmedaJR/PycharmProjects/telegram_bot/main.py', shell=False) == 0:
    print("fsd")