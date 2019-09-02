import requests
from bs4 import BeautifulSoup
import socket
from colorama import init

init()


def get_html(site):
    r = requests.get(site)
    return r.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    head = soup.find('thead').find_all('tr')
    line = soup.find('table', id='theProxyList').find('tbody').find_all('tr')

    for tr in head:
        th = tr.find_all('th')
        ip1 = th[1].text
        port1 = th[2].text
        country1 = th[3].text.replace('\xa0', '')
        anonym1 = th[4].text.replace('\r\n        ', '')
        types1 = th[5].text.replace('\r\n\t\t\t\t\t', '').replace('\r\n        ', '')
        time1 = th[6].text

        data1 = (ip1, port1, country1, anonym1, types1, time1)
        print(", ".join([str(s) for s in data1]))

        for tr in line:
            td = tr.find_all('td')
            ip = td[1].text
            port = td[2].text
            country = td[3].text.replace('\xa0', '')
            anonym = td[4].text.replace('\r\n        ', '')
            types = td[5].text.replace('\r\n\t\t\t\t\t', '').replace('\r\n        ', '')
            time = td[6].text

            data = (ip, port, country, anonym, types, time)
            print(", ".join([str(s) for s in data]))

            ### проверка порта прокси
            s = socket.socket()
            s.settimeout(4)  ### сколько ждать соеденения с портом прокси
            print('try proxy\033[93m', ip + ':' + port, '\033[00m')
            try:
                s.connect((ip, int(port)))
            except socket.error:
                s.close()
                print('port closed! proxy \033[31m' + ip + ':' + port, '!UNAVAILABLE!\033[00m')
            else:
                s.close()
                with open('proxy_list_checked0.txt', 'a') as fa:
                    print('proxy:\033[32m', ip + ':' + port, 'AVAILABLE\033[00m and written to file')
                    fa.write(ip + ':' + port + '\n')


def main():
    url = 'http://foxtools.ru/Proxy'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()