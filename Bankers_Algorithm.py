# Banker's Algorithm in Python
def calculate_need(maximum, allocation, n, m):
    need = []
    for i in range(n):
        need.append([maximum[i][j] - allocation[i][j] for j in range(m)])
    return need

def is_safe(available, maximum, allocation, n, m):
    need = calculate_need(maximum, allocation, n, m)
    work = available[:]
    finish = [False] * n
    safe_sequence = []

    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    for j in range(m):
                        work[j] += allocation[i][j]
                    safe_sequence.append(i)
                    finish[i] = True
                    found = True
                    break

        if not found:
            print("The system is in an unsafe state!")
            return False

    print("The system is in a safe state.")
    print("Safe sequence is:", ' '.join([f"P{p}" for p in safe_sequence]))
    return True

if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    m = int(input("Enter the number of resource types: "))

    available = list(map(int, input("Enter the available resources: ").split()))

    maximum = []
    print("Enter the maximum resource matrix (Max):")
    for i in range(n):
        maximum.append(list(map(int, input(f"For process P{i}: ").split())))

    allocation = []
    print("Enter the allocation resource matrix (Allocation):")
    for i in range(n):
        allocation.append(list(map(int, input(f"For process P{i}: ").split())))
    
    is_safe(available, maximum, allocation, n, m)