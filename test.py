import datetime
import threading
import urllib.request


def request():
    urllib.request.urlopen("http://127.0.0.1:5000")


threads = []

print(datetime.datetime.now())

for index in range(1000):
    x = threading.Thread(target=request, name=f't{index}')
    threads.append(x)

for y in threads:
    y.start()

for y in threads:
    y.join()

print(datetime.datetime.now())
