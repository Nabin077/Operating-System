# Python3 program for Highest Response Ratio Next (HRRN) Scheduling
def sort_by_arrival(processes, n):
    # Sorting based on arrival time using selection sort
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if processes[i]['arrival_time'] > processes[j]['arrival_time']:
                processes[i], processes[j] = processes[j], processes[i]

# Driver code
if __name__ == '__main__':
    
    sum_bt = 0  # Total burst time
    avgwt = 0   # Average waiting time
    avgtt = 0   # Average turnaround time
    n = 5       # Number of processes

    completed = [0] * n      # To track completed processes
    waiting_time = [0] * n   # To store waiting times of processes
    turnaround_time = [0] * n  # To store turnaround times of processes
    
    # Predefined arrival times and burst times
    arrival_time = [0, 2, 4, 6, 8]
    burst_time = [3, 6, 4, 5, 2]
    
    processes = []
    
    # Initializing processes with their respective arrival and burst times
    for i in range(0, n):
        processes.append({
            'process_id': chr(65 + i),  # Process names A, B, C, etc.
            'arrival_time': arrival_time[i],
            'burst_time': burst_time[i],
            'waiting_time': 0,
            'turnaround_time': 0
        })
        sum_bt += burst_time[i]
        
    # Sort processes by arrival time
    sort_by_arrival(processes, n)
    
    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    
    t = processes[0]['arrival_time']  # Start time is the first process's arrival time
    
    # Loop while there are processes left to schedule
    while sum(completed) < n:
        hrr = -1  # Highest response ratio
        loc = -1  # Index of process with highest response ratio

        # Find the process with the highest response ratio
        for i in range(n):
            if (processes[i]['arrival_time'] <= t) and not completed[i]:
                response_ratio = (processes[i]['burst_time'] + (t - processes[i]['arrival_time'])) / processes[i]['burst_time']
                
                if response_ratio > hrr:
                    hrr = response_ratio
                    loc = i

        if loc == -1:
            # If no process has arrived yet, increment the time
            t += 1
            continue

        # Process the selected process
        t += processes[loc]['burst_time']
        processes[loc]['waiting_time'] = t - processes[loc]['arrival_time'] - processes[loc]['burst_time']
        processes[loc]['turnaround_time'] = t - processes[loc]['arrival_time']
        
        # Mark the process as completed
        completed[loc] = 1

        # Accumulate waiting time and turnaround time for averages
        avgwt += processes[loc]['waiting_time']
        avgtt += processes[loc]['turnaround_time']

        # Print the process details
        print(f"{processes[loc]['process_id']}\t\t{processes[loc]['arrival_time']}\t\t{processes[loc]['burst_time']}\t\t{processes[loc]['waiting_time']}\t\t{processes[loc]['turnaround_time']}")

    # Calculate and print average waiting time and turnaround time
    print("Average Waiting Time: {:.2f}".format(avgwt / n))
    print("Average Turnaround Time: {:.2f}".format(avgtt / n))
