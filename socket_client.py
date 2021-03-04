import socket

try:
    import config
    ip = config.host
    port = config.sock_port
except:
    ip = input("Введите ip сервера: ")
    port = int(input("Введите port сервера: "))


sock = socket.socket()
sock.connect((ip, port))

while True:
    try:
        print(sock.recv(1024).decode("utf-8"))
    except:
        sock.close()
