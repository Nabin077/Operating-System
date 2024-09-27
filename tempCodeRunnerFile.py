import multiprocessing
import time
import os
import sys

# Function to be executed by the child process
def child_process():
    print(f"Child process {os.getpid()} started")
    time.sleep(5)  # Simulating work by sleeping
    print(f"Child process {os.getpid()} finished")

if __name__ == '__main__':
    try:
        print(f"Parent process {os.getpid()} started")

        # Create a new child process
        process = multiprocessing.Process(target=child_process)

        # Start the child process
        process.start()

        # Simulate some work in the parent process
        time.sleep(2)

        # Terminate both the child and the parent processes
        if process.is_alive():
            print(f"Terminating child process {process.pid}")
            process.terminate()

        # Wait for the child process to terminate
        process.join()

        print(f"Parent process {os.getpid()} exiting")
        sys.exit()  # Gracefully exit the parent process

    except KeyboardInterrupt:
        print("Process interrupted")
        sys.exit()
