



# 1. Point-to-Point Communication
Demonstrates inter-process communication using the `mpi4py` library:  
- Processes communicate using the `send` and `recv` methods.  
- Data is transmitted between specific processes identified by their ranks.  
This example showcases how processes can exchange data effectively in an MPI environment.

## Output
![Code Screenshot](outputs-ss/image1.png)

## Explanation
1. **Ranks Involved in Communication**:
   - **Rank 0** sends an integer to **Rank 4**.
   - **Rank 1** sends a string to **Rank 8**.

2. **Other Ranks**:
   - Ranks not involved print their own rank.


# 2. Deadlock Problem
Demonstrates a classic deadlock scenario using the `mpi4py` library:  
- Processes communicate using `send` and `recv` methods.  
- Deadlock can occur when two processes wait for each other to send and receive data, leading to a halt in execution.

## Output
![Code Screenshot](outputs-ss/image2.png)

## Explanation
1. **Ranks Involved in Communication**:
   - **Rank 1** sends `"a"` to **Rank 5** and waits to receive data from **Rank 5**.
   - **Rank 5** sends `"b"` to **Rank 1** and waits to receive data from **Rank 1**.

2. **Deadlock Issue**:
   - **Rank 1** sends data to **Rank 5** and waits to receive data from **Rank 5**.
   - **Rank 5** sends data to **Rank 1** and waits to receive data from **Rank 1**.
   - Both ranks wait for each other, causing a deadlock where neither can proceed. This happens because they both need to send and receive data simultaneously, but neither can do so because each is waiting on the other.

3. **Other Ranks**:
   - Ranks not involved in the communication simply print their rank and do not participate in the deadlock.


# 3. Broadcast Communication
Demonstrates the concept of broadcasting using the `mpi4py` library:  
- The root process (Rank 0) broadcasts a variable to all other processes.  
- All processes, regardless of rank, receive the same value from the root.

## Output
![Code Screenshot](outputs-ss/image3.png)

## Explanation
1. **Rank 0**:
   - **Rank 0** initializes the variable `variable_to_share` with the value `100`.
   - The value is broadcasted to all other processes using the `comm.bcast` method.

2. **Other Ranks**:
   - All other ranks (1, 2, 3, 4, 5, 6, 7, 8) receive the value `100` from **Rank 0** and print it.
   - The broadcast ensures that each process gets the same value, regardless of its rank.
