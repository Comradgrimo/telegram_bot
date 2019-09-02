

def parser():
    from grab import Grab
    import re
    import socket
    g = Grab()
    try:
        g.go('http://spys.one/socks/')
    except:
        print("Перезапускаю коннект")
        g.go('http://spys.one/socks/')
    ip=[]
    proxy=[]
    port="1080"
    for elem in g.doc.select('//td[@colspan="1"]/font[@class="spy14"]'):
        ip.append(elem.text()[0:20])
    ip = [re.sub('[^1234567890.]', '', i) for i in ip]
    ip = ip[::2]
    for i in range(len(ip)):
        s = socket.socket()
        try:
            s.connect((ip[i], int(port)))
            s.settimeout(100)
            print("Найден IP " + ip[i] + ':' + port)
            proxy.append(ip[i])
        except socket.error:
            s.close()
            print('IP не работает ' + ip[i] + ':' + port)
    print("work proxy =" , proxy)
    return proxy


if __name__ == "__main__":
    print('Теперь ничего не сломается!')
