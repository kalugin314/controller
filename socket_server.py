import time
import socket
from colorama import init, Fore

init()

try:
    import config
    address = config.host
    port = config.sock_port
except ModuleNotFoundError:
    print(Fore.RED + "ERROR: оцуцтвует конфиг")
    raise Exception


def start():

    sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock_server.bind((address, port))
    sock_server.listen(100)
    print(sock_server.getsockname())
    while True:
        client_sock, client_addr = sock_server.accept()
        print("Connection from : ", client_addr)
        file = open("connected.txt", "w")
        file.write("1")
        file.close()
        while True:
            try:
                file = open("msg.txt", "r")
                msg = file.read()
                file.close()
                time.sleep(0.1)
                print(msg)
                client_sock.send(msg.encode("utf-8"))
            except:
                client_sock.close()
                print("Disconnection from : ", client_addr)
                file = open("connected.txt", "w")
                file.write("0")
                file.close()
                break


if __name__ == "__main__":
    start()

