class Process:
    def __init__(self, pid, arrival, burst, priority):
        self.id = pid
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.completion = 0
        self.waiting = 0
        self.turnaround = 0

def sort_by_arrival(processes):
    # Sorting processes by arrival time
    processes.sort(key=lambda x: x.arrival)

def sort_by_priority(processes, start):
    # Sorting processes by priority (higher number means higher priority)
    processes[start:] = sorted(processes[start:], key=lambda x: -x.priority)

def calculate_times(processes):
    current_time = 0
    for process in processes:
        if current_time < process.arrival:
            current_time = process.arrival
        process.completion = current_time + process.burst
        process.turnaround = process.completion - process.arrival
        process.waiting = process.turnaround - process.burst
        current_time = process.completion

def print_results(processes):
    total_waiting = 0
    total_turnaround = 0
    print("\nProcess\tArrival Time\tBurst Time\tPriority\tCompletion Time\tWaiting Time\tTurnaround Time")
    for process in processes:
        total_waiting += process.waiting
        total_turnaround += process.turnaround
        print(f"{process.id}\t{process.arrival}\t\t{process.burst}\t\t{process.priority}\t\t{process.completion}\t\t{process.waiting}\t\t{process.turnaround}")
    
    avg_waiting_time = total_waiting / len(processes)
    avg_turnaround_time = total_turnaround / len(processes)
    print(f"\nAverage waiting time = {avg_waiting_time:.2f}")
    print(f"Average turnaround time = {avg_turnaround_time:.2f}")

def main():
    n = int(input("Enter the number of processes: "))
    
    processes = []
    for i in range(n):
        arrival = int(input(f"Enter arrival time for process {i + 1}: "))
        burst = int(input(f"Enter burst time for process {i + 1}: "))
        priority = int(input(f"Enter priority (higher number indicates higher priority) for process {i + 1}: "))
        processes.append(Process(i + 1, arrival, burst, priority))
    
    sort_by_arrival(processes)  # Sort processes by arrival time initially
    
    # Move process with arrival time 0 to the front, then sort by priority
    if processes[0].arrival == 0:
        sort_by_priority(processes, 1)
    else:
        sort_by_priority(processes, 0)
    
    calculate_times(processes)  # Calculate completion, waiting, and turnaround times
    print_results(processes)  # Print the scheduling results

if __name__ == "__main__":
    main()
