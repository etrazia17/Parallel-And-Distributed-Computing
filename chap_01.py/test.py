import threading
import time

def calc_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return calc_fibonacci(n-1) + calc_fibonacci(n-2)

threads = []

# Start timing
start_time = time.time()

for i in range(9):
    t = threading.Thread(target=calc_fibonacci, args=(40,))
    threads.append(t)
    print(f"Starting thread {i+1}")
    t.start()

for t in threads:
    t.join()

# End timing
end_time = time.time()

# Calculate and print execution time
print(f"Total execution time: {end_time - start_time:.4f} seconds")
