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
# import subprocess
# if subprocess.call('python C:/Users/ReshmedaJR/PycharmProjects/telegram_bot/main.py', shell=False) == 0:
#     print("fsd")
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from lxml import html
from lxml import etree
import re
import io
import socket
driver = webdriver.Chrome("C://Users/ReshmedaJR/PycharmProjects/telegram_bot/chromedriver.exe")
driver.get("https://hidemy.name/ru/proxy-list/?type=5#list")
sleep(5)
elem = driver.find_element_by_xpath("//*")
source_code = elem.get_attribute("outerHTML")
f = open('telegram_bot/html/html_source_code.html', 'w', encoding='utf-8')
f.write(source_code)
f.close()
html_report_part1 = open('telegram_bot/html/html_source_code.html','r', encoding='utf-8')
soup = BeautifulSoup(html_report_part1, 'html.parser')
ip=[]

#ПОЛУЧАЕМ ВСЕ IP
result = soup.find_all(class_="tdl")
for i in range(len(result)):
    ip.append(str(result[i].renderContents()))
ipp = [re.sub('[^1234567890. ]', '', i) for i in ip]
print("Ip Получены")

#ПОЛУЧАЕМ ПОРТЫ
port=[]
list_ip = []
soup_str = (''.join(soup.prettify().splitlines()).replace(' ', ''))
ipport = [re.findall('<td>\d{4,5}</td>',soup_str)]
for i in range(len(ipport[0])):
    port.append([re.findall('\d{4,5}',str(ipport[0][i]))])
print("Порты Получены")
#IP + PORT
for i in range(len(ipp)):
    list_ip.append(((ipp[i],port[i][0][0])))

#ПРОВЕРКА
proxy=[]
for i in range(len(list_ip)):
    s = socket.socket()
    try:
        s.connect((list_ip[i][0], int(list_ip[i][1])))
        s.settimeout(100)
        print("Найден IP " + list_ip[i][0] + ':' + (list_ip[i][1]))
        proxy.append(list_ip[i][0] + ':' + (list_ip[i][1]))
    except socket.error:
        s.close()
        print('IP не работает ' + list_ip[i][0] + ':' + (list_ip[i][1]))
print("work proxy =", proxy)



#print(soup.find_all(("td1", {"td"})))
#p_element = (driver.find_element_by_class_name("td1").text)
# a = p_element.split('\n')
# b,c,d=[],[],[]
# for i in range(len(a)):
#     b.append(a[i][0:20])
# ipport = [re.sub('[^1234567890. ]', '', i) for i in b]
# for i in range(len(ipport)):
#     c.append(ipport[i].split(' '))
# for i in range(len(c)):
#     d.append([x for x in c[i] if x != ''])
# d.remove([])
#
# proxy = []
# s = socket.socket()
#
# for i in range(len(d)):
#     s = socket.socket()
#     try:
#         s.connect((d[i][0], int(d[i][1])))
#         s.settimeout(100)
#         print("Найден IP " + d[i][0] + ':' + (d[i][1]))
#         proxy.append(d[i][0] + ':' + (d[i][1]))
#     except socket.error:
#         s.close()
#         print('IP не работает ' + d[i][0] + ':' + (d[i][1]))
# print("work proxy =" , proxy)