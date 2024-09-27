class Process:
    def __init__(self, pid, arrival, burst):
        self.pid = pid  # Process ID
        self.arrival = arrival  # Arrival Time
        self.burst = burst  # Burst Time
        self.remaining = burst  # Remaining Time (initially equal to burst time)
        self.completion = 0  # Completion Time
        self.waiting = 0  # Waiting Time
        self.turnaround = 0  # Turnaround Time

def sort_by_arrival(processes):
    # Sort the list of processes based on arrival time
    processes.sort(key=lambda x: x.arrival)

def calculate_times(processes):
    time = 0
    completed = 0
    n = len(processes)
    is_completed = [False] * n  # Track completion of processes
    execution_order = []  # To track execution order of processes

    # Initialize remaining burst time for each process
    for process in processes:
        process.remaining = process.burst

    while completed != n:
        min_remaining = float('inf')
        shortest = -1

        # Find process with shortest remaining time that has arrived
        for i in range(n):
            if processes[i].arrival <= time and not is_completed[i] and processes[i].remaining < min_remaining:
                min_remaining = processes[i].remaining
                shortest = i

        if shortest == -1:
            time += 1  # No process is available, increment time
        else:
            execution_order.append(processes[shortest].pid)
            processes[shortest].remaining -= 1
            time += 1

            # If the process has finished executing
            if processes[shortest].remaining == 0:
                processes[shortest].completion = time
                processes[shortest].turnaround = processes[shortest].completion - processes[shortest].arrival
                processes[shortest].waiting = processes[shortest].turnaround - processes[shortest].burst
                is_completed[shortest] = True
                completed += 1

    return execution_order

def print_results(processes, execution_order):
    total_waiting = 0
    total_turnaround = 0

    print("\nProcess\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    for process in processes:
        total_waiting += process.waiting
        total_turnaround += process.turnaround
        print(f"{process.pid}\t\t{process.arrival}\t\t{process.burst}\t\t{process.completion}\t\t{process.waiting}\t\t{process.turnaround}")

    avg_waiting = total_waiting / len(processes)
    avg_turnaround = total_turnaround / len(processes)
    
    print(f"\nAverage waiting time = {avg_waiting:.2f}")
    print(f"Average turnaround time = {avg_turnaround:.2f}")

def main():
    n = int(input("Enter the number of processes: "))
    processes = []

    # Input the arrival time and burst time for each process
    for i in range(n):
        arrival, burst = map(int, input(f"Enter arrival time and burst time for process {i+1}: ").split())
        processes.append(Process(i+1, arrival, burst))

    sort_by_arrival(processes)
    execution_order = calculate_times(processes)
    print_results(processes, execution_order)

if __name__ == "__main__":
    main()
