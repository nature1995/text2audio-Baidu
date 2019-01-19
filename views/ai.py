from flask import Flask,request,render_template
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket

app = Flask(__name__,template_folder="../templates")

@app.route("/index")
def index():
    # 获取请求的WebSocket对象
    user_socket = request.environ.get("wsgi.websocket") # type:WebSocket
    print(user_socket)  # <geventwebsocket.websocket.WebSocket object at 0x000002718C07F798>
    print(request.remote_addr)  # 远程ip地址127.0.0.1
    while True:
        # 接收消息
        msg = user_socket.receive()
        print(msg)

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    http_serv = WSGIServer(("0.0.0.0",9520),app,handler_class=WebSocketHandler)
    http_serv.serve_forever()