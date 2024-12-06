import time
import multiprocessing
import threading

def do_something(size, out_list):
    # Dummy processing for demonstration
    for i in range(size):
        out_list.append(i * i)

if __name__ == "__main__":
    size = 20000  # Fixed size assignment
    procs = 10
    jobs = []

    # Multiprocessing
    start_time = time.time()
    for i in range(procs):
        out_list = []  # Each process needs its own list
        process = multiprocessing.Process(target=do_something, args=(size, out_list))
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("List processing complete (Multiprocessing).")
    end_time = time.time()
    print(f"Multiprocessing time: {end_time - start_time} seconds")

    # Reset jobs list for threading
    jobs = []
    threads = 10
    start_time = time.time()
    for k in range(threads):
        out_list = []  # Each thread needs its own list
        thread = threading.Thread(target=do_something, args=(size, out_list))
        jobs.append(thread)

    for l in jobs:
        l.start()

    for l in jobs:
        l.join()

    print("List processing complete (Multithreading).")
    end_time = time.time()
    print(f"Multithreading time: {end_time - start_time} seconds")
