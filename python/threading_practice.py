import threading
import time

lock = threading.Lock()
count = 0

def counter():
    global count
    for _ in range(100000):
        with lock:
            count += 1
            print(count)

t1 = threading.Thread(target=counter, name="Thread-1", daemon=True)
t2 = threading.Thread(target=counter, name="Thread-2", daemon=True)

t1.start()
t2.start()

t1.join()
t2.join()