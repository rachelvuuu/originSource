
import time
from flask import Response

def handler(request):
    time.sleep(10)
    return Response("Read delay simulation", status=200)
