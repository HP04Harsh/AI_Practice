import multiprocessing
import time

def square(num, q, counter):
    result = num * num
    q.put(result)
    counter.value += 1

if __name__ == '__main__':
    numbers = [1,2,3,4,5]
    q = multiprocessing.Queue()
    counter = multiprocessing.Value('i', 0)  # Shared counter
    processes = []

    for num in numbers:
        p = multiprocessing.Process(target=square, args=(num, q, counter))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    results = []
    while not q.empty():
        results.append(q.get())
        counter.value -= 1
    print("Results:", results)
    print("Counter:", counter.value)  # Should be 0 if all processes completed successfully    