import socket

ip = '118.24.63.167'
port = '1113'

s = socket.socket()
s.settimeout(10000)  ### сколько ждать соеденения с портом прокси
print('try proxy', ip + ':' + port)
try:
    s.connect((ip, int(port)))
    print("it's ok")
except socket.error:
    s.close()
    print('port closed!' + ip + ':' + port, '!UNAVAILABLE!')
else:
    s.close()