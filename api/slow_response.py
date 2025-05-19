
from flask import Response
import time

def handler(request):
    def generate():
        for i in range(5):
            yield f"Line {i+1}\n"
            time.sleep(1)
    return Response(generate(), mimetype="text/plain")
