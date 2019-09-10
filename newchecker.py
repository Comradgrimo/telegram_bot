import socket

ip = '199.189.27.34'
port = '1080'

s = socket.socket()
s.settimeout(1000)  ### сколько ждать соеденения с портом прокси
print('try proxy', ip + ':' + port)
try:
    s.connect((ip, int(port)))
    print("it's ok")
except socket.error:
    s.close()
    print('port closed!' + ip + ':' + port, '!UNAVAILABLE!')
else:
    s.close()