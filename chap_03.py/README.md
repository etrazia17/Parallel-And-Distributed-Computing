## **Chapter 3: Process-Based Parallelism**

Process-based parallelism allows programs to achieve true parallel execution by running multiple processes simultaneously. This approach leverages multiple CPU cores, making it more suitable for CPU-intensive tasks than threads.

### **Why Use Processes?**
1. **Isolation:** Processes have their own memory space, preventing conflicts.
2. **Scalability:** Processes utilize multiple cores for parallel execution.
3. **Reliability:** Crashes in one process do not affect others.

### **1. communicating_with_pipe.py**
Demonstrates inter-process communication using pipes:
- Processes send and receive data through a pipe.
- Ensures unidirectional or bidirectional data flow.
This example showcases how processes can communicate effectively.

### **2. communicating_with_queue.py**
Uses a queue for inter-process communication:
- Processes place and retrieve data from a shared queue.
- Ensures thread-safe and efficient communication.
This approach is ideal for task distribution.

### **3. killing_processes.py**
Illustrates how to terminate processes:
- Spawns multiple processes and kills them programmatically.
- Demonstrates clean termination to avoid resource leaks.
This is essential for managing long-running applications.

### **4. naming_processes.py**
Assigns names to processes for better organization:
- Processes are named for easier identification.
- Useful for debugging and logging.
This enhances process manageability.

### **5. process_in_subclass.py**
Shows how to create and manage processes in custom subclasses:
- A class-based approach to process management.
- Encapsulates process logic for reusability.
This is useful for structured multiprocessing.

### **6. process_pool.py**
Demonstrates parallel execution using a process pool:
- Spawns a pool of worker processes to handle tasks.
- Distributes tasks automatically across available workers.
This is ideal for efficiently managing large task volumes.

### **7. processes_barrier.py**
Illustrates process synchronization using barriers:
- Processes perform tasks and wait at a barrier.
- Ensures all processes complete a phase before moving forward.
This is crucial for coordination in multi-step workflows.

### **8. run_background_processes.py**
Runs processes in the background:
- Demonstrates non-blocking execution.
- Useful for background tasks and daemons.
This improves application responsiveness.

### **9. run_background_processes_no_daemons.py**
Explains background processes without using daemons:
- Processes execute in the background but are not daemonic.
- Ensures they finish execution properly.
This is suitable for tasks requiring completion.

### **10. spawning_processes.py**
Basic example of spawning new processes:
- Creates multiple processes to execute tasks concurrently.
- Demonstrates the foundational concepts of multiprocessing.
This is a starting point for parallel programming.

### **11. spawning_processes_namespace.py**
Explains process namespaces:
- Spawns processes with shared namespaces for variable access.
- Demonstrates shared data management.
This is useful for inter-process collaboration.

### **12. denom.py**
A utility script demonstrating error handling or related concepts:
- Handles specific scenarios in multiprocessing workflows.
- Ensures robustness in process-based applications.
The exact purpose depends on its implementation.

## Requirements
Ensure you have Python 3.6 or later installed. To install additional dependencies, if any, run:

```bash
pip install -r requirements.txt
```

## Usage
To run any script, use the following command:

```bash
python <script_name>.py
```

For example, to run the script for inter-process communication using queues:

```bash
python communicating_with_queue.py
```