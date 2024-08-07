import time
import threading
import requests
import multiprocessing

def do_something(index):
    print('Process started ...')
    res = requests.get("https://picsum.photos/200/300")
    with open(f'images/image-{index}.png', 'wb') as file:
        file.write(res.content)
    print('Process ended ...')

t1 = time.time()

threads = []

for i in range(100):
    th = multiprocessing.Process(target=do_something, args=(i,))
    th.start()
    threads.append(th)

for i in threads:
    i.join()

t2 = time.time()

print(t2 - t1)