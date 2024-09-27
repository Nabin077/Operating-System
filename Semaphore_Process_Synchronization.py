import os
import time
import multiprocessing
from multiprocessing import Semaphore

# Semaphore initialization function
def init_semaphore():
    # Create a semaphore with an initial value of 1
    return Semaphore(1)

# Wait (P) operation
def semaphore_wait(sem):
    sem.acquire()

# Signal (V) operation
def semaphore_signal(sem):
    sem.release()

# Critical section function for processes
def critical_section(sem):
    semaphore_wait(sem)
    
    # Critical section
    pid = os.getpid()
    print(f"Process {pid} is in the critical section")
    time.sleep(1)  # Simulate some work in the critical section
    print(f"Process {pid} is leaving the critical section")
    
    semaphore_signal(sem)

if __name__ == "__main__":
    # Initialize the semaphore
    sem = init_semaphore()

    # Create a list to store child processes
    processes = []

    # Create 5 child processes
    for i in range(5):
        p = multiprocessing.Process(target=critical_section, args=(sem,))
        processes.append(p)
        p.start()

    # Wait for all child processes to complete
    for p in processes:
        p.join()

    print("All processes have finished.")