
import time
from flask import Response

def handler(request):
    time.sleep(10)
    return Response("Simulated connect timeout", status=504)
