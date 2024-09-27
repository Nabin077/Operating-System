import threading
import time
import random

# Constants
NUM_PHILOSOPHERS = 3
MAX_EAT_TIMES = 2

# Semaphores for forks
forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]

# Mutex for managing critical section (picking up forks)
mutex = threading.Lock()

def philosopher(id):
    left = id
    right = (id + 1) % NUM_PHILOSOPHERS
    eat_count = 0

    while eat_count < MAX_EAT_TIMES:
        # Thinking
        print(f"Philosopher {id} is thinking.")
        time.sleep(random.uniform(1, 2))

        # Pick up forks
        with mutex:
            forks[left].acquire()  # Pick up left fork
            forks[right].acquire()  # Pick up right fork

        # Eating
        print(f"Philosopher {id} is eating.")
        eat_count += 1
        time.sleep(random.uniform(1, 2))  # Simulate eating time

        # Put down forks
        forks[left].release()  # Put down left fork
        forks[right].release()  # Put down right fork

    print(f"Philosopher {id} has finished eating {eat_count} times and leaves the table.")

def main():
    # Create and start philosopher threads
    philosophers = []
    for i in range(NUM_PHILOSOPHERS):
        t = threading.Thread(target=philosopher, args=(i,))
        philosophers.append(t)
        t.start()

    # Wait for all philosophers to finish
    for t in philosophers:
        t.join()

if __name__ == "__main__":
    main()
