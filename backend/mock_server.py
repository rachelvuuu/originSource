from flask import Flask, Response, request
from flask_sock import Sock
import time

app = Flask(__name__)
sock = Sock(app)

@app.route('/slow-response')
def slow_response():
    def generate():
        for i in range(5):
            yield f"Line {i+1}\n"
            time.sleep(1)
    return Response(generate(), mimetype='text/plain')

@app.route('/simulate-connect-timeout')
def simulate_connect_timeout():
    time.sleep(10)
    return "Simulated connect timeout", 504

@app.route('/simulate-send-timeout', methods=['POST'])
def simulate_send_timeout():
    time.sleep(10)
    return "Send timeout simulation complete", 200

@app.route('/simulate-read-timeout')
def simulate_read_timeout():
    time.sleep(10)
    return "Read delay simulation", 200

@sock.route('/ws')
def websocket_echo(ws):
    while True:
        msg = ws.receive()
        if msg is None:
            break
        ws.send(f"Echo: {msg}")

if __name__ == '__main__':
    app.run(port=8080)