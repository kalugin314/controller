from flask import Flask, render_template, session
from flask_socketio import SocketIO, send
from colorama import init, Fore

init()

try:
    import config
    host = config.host
    port = config.port
except ModuleNotFoundError:
    print(Fore.RED + "ERROR: оцуцтвует конфиг")
    raise Exception

app = Flask(__name__)

sio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def index():
    return render_template("index.html", host=host + ":" + str(port))


@sio.on("message")
def onmessage(msg1):
    file = open("msg.txt", "w")
    file.write(msg1)
    file.close()
    file = open("connected.txt", "r")
    send(file.read())
    file.close()


if __name__ == "__main__":
    app.debug = True
    sio.run(app, host=host, port=port)
