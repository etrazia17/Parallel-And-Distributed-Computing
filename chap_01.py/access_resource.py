import threading
import time

# Initialize a semaphore with a maximum of 2 threads allowed to access the resource at a time
sem = threading.Semaphore(2)

def access_resource(thread_name):
    sem.acquire()  # Acquires a semaphore, blocking if necessary until it is available
    print(f"{thread_name} accessing the resource")
    time.sleep(2)  # Simulates the time taken to access the resource
    print(f"{thread_name} done")
    sem.release()  # Releases the semaphore

threads = []
for i in range(5):
    t = threading.Thread(target=access_resource, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
