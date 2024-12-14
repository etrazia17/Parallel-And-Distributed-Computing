from multiprocessing import Process, Queue

def producer (queue):
    for i in range(5):
