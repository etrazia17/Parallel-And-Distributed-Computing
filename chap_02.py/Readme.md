## **Chapter 2: Thread-Based Parallelism**

Thread-based parallelism allows programs to run faster by performing multiple tasks at the same time. Instead of running tasks sequentially, threads make it possible to execute them in parallel, improving responsiveness and performance.

### **Why Use Threads?**  
1. **Efficiency:** Threads split work into smaller tasks, making programs faster.  
2. **Responsiveness:** Threads keep programs responsive, even during heavy tasks.  
3. **Resource Sharing:** Threads can share memory and resources for quicker communication.
### **1. Barrier.py**  
Simulates a race with three runners:  
- Each runner is represented by a thread.  
- Threads simulate different speeds using random delays.  
- A barrier ensures all threads finish together before the race ends.  
This helps to understand thread synchronization using barriers.

---

### **2. Condition.py**  
Implements a producer-consumer pattern using a shared list and condition variables:  
- **Producer:** Adds items to the list and notifies the consumer.  
- **Consumer:** Removes items and alerts the producer when space is available.  
This ensures efficient teamwork between producer and consumer without conflicts.

---

### **3. Event.py**  
Uses an `Event` object for thread communication:  
- **Producer:** Signals the consumer when items are ready.  
- **Consumer:** Waits for the signal, then processes the items.  
This method improves thread coordination and resource usage.

---

### **4. MyThreadClass.py**  
Custom thread class example:  
- Threads perform tasks like random delays and printing their name.  
- `join()` ensures the main program waits for all threads to finish.  
This demonstrates how threading can run tasks simultaneously for better efficiency.

---

### **5. MyThreadClass_lock.py**  
Demonstrates thread synchronization using locks:  
- Threads lock shared resources while using them and release the lock after.  
- This avoids overlapping and ensures proper order in outputs.  

---

### **6. MyThreadClass_lock2.py**  
Focuses on safely sharing resources using locks:  
- Threads acquire a shared lock before performing tasks and release it afterward.  
- `join()` ensures all threads finish before the program ends.  
Locks provide a structured way to handle shared resources without errors.

---

### **7. Rlock.py**  
Uses `RLock` (Reentrant Lock) for adding and removing items from a shared box:  
- Two threads handle addition and removal concurrently.  
- The lock ensures synchronized access to the shared resource.  
This demonstrates thread-safe operations while maintaining concurrency.

---

### **8. Semaphore.py**  
Illustrates semaphores for synchronization in a producer-consumer setup:  
- **Producer:** Creates random numbers and signals the consumer.  
- **Consumer:** Processes numbers after receiving the signal.  
Semaphores ensure orderly communication between threads.

---

### **9. Thread_defination.py**  
Shows basic thread management:  
- A single function runs multiple threads, each with a unique number.  
- `join()` ensures all threads finish before the program ends.  
This is a simple way to understand parallel task execution.

---

### **10. Thread_determine.py**  
Runs three functions concurrently using threads:  
- Threads start, sleep for a short duration, and then exit.  
- The program waits for all threads to complete using `join()`.  
This is a straightforward example of multithreading.

---

### **11. Thread_name_and_processes.py**  
Demonstrates how two threads can run side by side:  
- Threads print simple messages and finish independently.  
- The main program waits for both threads to complete.  
This showcases the basics of parallel execution.

---

### **12. Thread_with_queue.py**  
Implements a producer-consumer pattern using a queue:  
- **Producer:** Adds random numbers to a queue.  
- **Consumers:** Monitor and process the queue in parallel.  
- `task_done()` ensures proper tracking of tasks.  
This setup enables efficient multitasking.

---