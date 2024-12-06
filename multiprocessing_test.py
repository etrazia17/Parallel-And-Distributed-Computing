from do something import *
import time
import multiprocessing
import threading

if _name_ == "_main_"

name main
size 20000
procs = 10
jobs = 11
#Multiprocessing
start time time.time()
for i in range(procs):
out list list()
process multiprocessing. Process(target-do_something, args=(size, out_list))
jobs.append(process)
for j in jobs:
j.start()
for j in jobs:
J.join()
print("List processing complete.")
end time time.time()
print("Multiprocessing time, end time start time)
Reset jobs List for threading
jobs = []
threads=10
start time = time.time()
for k in range(threads):
out list List()
thread threading.Thread(target-do something, args=(size, out list)) Corrected to pass the function reference
jobs.append(thread)
for 1 in jobs:
L.start()
for in jobs: L.join()
print("List processing complete.")
end time = time.time()
print("Multithreading time, end time start time