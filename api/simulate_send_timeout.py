
import time
from flask import Response

def handler(request):
    time.sleep(10)
    return Response("Send timeout simulation complete", status=200)
