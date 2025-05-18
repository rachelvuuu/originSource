import socket
import time
import argparse

parser = argparse.ArgumentParser(description="Simulate delayed HTTP headers")
parser.add_argument("host", help="CDN domain to connect to")
parser.add_argument("--delay", type=int, default=30, help="Delay before completing headers (seconds)")
args = parser.parse_args()

host = args.host
delay = args.delay
port = 80

print(f"🌐 Connecting to {host} with header delay of {delay}s...")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.send(b"GET /api/delay-header HTTP/1.1\r\n")
time.sleep(delay)
s.send(f"Host: {host}\r\nConnection: close\r\n\r\n".encode())

try:
    response = s.recv(1024)
    print("✅ Response received:")
    print(response.decode())
except Exception as e:
    print(f"❌ Error receiving response: {e}")
finally:
    s.close()