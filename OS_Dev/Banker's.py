def is_safe(available, max_demand, allocation, need, num_processes, num_resources):
    work = available[:]  # Copy of available resources
    finish = [False] * num_processes  # List to track if process is finished
    safe_sequence = []  # List to store the safe sequence
    
    # While there are processes not yet finished
    while len(safe_sequence) < num_processes:
        allocated_in_this_round = False
        
        # Try to allocate resources to a process if needed
        for i in range(num_processes):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(num_resources)):  # Process i can be allocated
                # Add allocated resources back to work
                for j in range(num_resources):
                    work[j] += allocation[i][j]
                
                finish[i] = True
                safe_sequence.append(i)  # Add process to safe sequence
                allocated_in_this_round = True
        
        # If no process was allocated in this round, then it's an unsafe state
        if not allocated_in_this_round:
            return False, []
    
    return True, safe_sequence

def main():
    num_processes = int(input("Enter number of processes: "))
    num_resources = int(input("Enter number of resources: "))
    
    # Get available resources
    available = list(map(int, input("Enter available resources (space-separated): ").split()))
    
    # Get maximum demand matrix
    max_demand = []
    print("Enter max demand matrix:")
    for i in range(num_processes):
        max_demand.append(list(map(int, input(f"Process {i}: ").split())))
    
    # Get allocation matrix
    allocation = []
    print("Enter allocation matrix:")
    for i in range(num_processes):
        allocation.append(list(map(int, input(f"Process {i}: ").split())))
    
    # Calculate the need matrix
    need = []
    for i in range(num_processes):
        need.append([max_demand[i][j] - allocation[i][j] for j in range(num_resources)])
    
    # Check if the system is in a safe state
    safe, safe_sequence = is_safe(available, max_demand, allocation, need, num_processes, num_resources)
    
    if safe:
        print("System is in a safe state.")
        print("Safe sequence:", " -> ".join("P{}".format(p) for p in safe_sequence))
    else:
        print("System is not in a safe state.")

if __name__ == "__main__":
    main()
