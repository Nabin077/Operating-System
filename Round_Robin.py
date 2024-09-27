def round_robin():
    n = int(input("Enter the number of processes (maximum 10): "))
    bt = [0] * n
    wt = [0] * n
    tat = [0] * n
    rem_bt = [0] * n
    
    print("Enter the burst time of the processes:")
    for i in range(n):
        bt[i] = int(input(f"P{i} = "))
        rem_bt[i] = bt[i]
    
    qt = int(input("Enter the quantum time: "))
    
    count = 0
    sq = 0
    awt = 0.0
    atat = 0.0
    
    while True:
        for i in range(n):
            temp = qt
            if rem_bt[i] == 0:
                count += 1
                continue
            if rem_bt[i] > qt:
                rem_bt[i] -= qt
            else:
                temp = rem_bt[i]
                rem_bt[i] = 0
            sq += temp
            tat[i] = sq

        if count == n:
            break
        count = 0  # Reset the count each loop

    # Printing the header
    print("-" * 60)
    print(f"{'Process':<10}{'Burst Time':<15}{'Turnaround Time':<20}{'Waiting Time'}")
    print("-" * 60)
    
    # Print details of each process
    for i in range(n):
        wt[i] = tat[i] - bt[i]
        awt += wt[i]
        atat += tat[i]
        print(f"P{i+1:<9}{bt[i]:<14}{tat[i]:<19}{wt[i]}")

    # Calculating averages
    awt /= n
    atat /= n
    print(f"\nAverage Waiting Time = {awt:.2f}")
    print(f"Average Turnaround Time = {atat:.2f}")

# Run the Round Robin function
round_robin()
