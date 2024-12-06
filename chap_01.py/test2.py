from concurrent.futures import ThreadPoolExecutor
import time

def task_1():
    print("Task 1 executed")

def task_2():
    print("Task 2 executed")

start_time = time.time()

with ThreadPoolExecutor() as executor:
    future1 = executor.submit(task_1)
    future2 = executor.submit(task_2)

# Ensure both tasks are completed
future1.result()
future2.result()

end_time = time.time()

execution_time = end_time - start_time
print(f"Total execution time: {execution_time} seconds")
