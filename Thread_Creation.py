import threading
import time

# Function that the thread will execute
def thread_worker(name):
    print(f"Thread {name} started")
    for i in range(2):  # Reduced to 2 iterations
        print(f"Thread {name} is running iteration {i}")
        time.sleep(1)  # Simulating some work
    print(f"Thread {name} finished")

# Create threads
thread1 = threading.Thread(target=thread_worker, args=("Worker 1",))
thread2 = threading.Thread(target=thread_worker, args=("Worker 2",))

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to complete
thread1.join()   
thread2.join()

print("Both threads have finished execution.")
