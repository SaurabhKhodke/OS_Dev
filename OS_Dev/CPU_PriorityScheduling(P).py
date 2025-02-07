import matplotlib.pyplot as plt

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time  # For preemption
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def priority_preemptive(processes):
    current_time = 0
    completed = 0
    gantt = []

    while completed != len(processes):
        # Get the list of processes that have arrived and have remaining time
        available_processes = [p for p in processes if p.arrival_time <= current_time and p.remaining_time > 0]

        if available_processes:
            # Select the process with the highest priority (lowest priority number)
            highest_priority_process = min(available_processes, key=lambda x: x.priority)

            start_time = current_time
            current_time += 1  # Simulate the process running for 1 time unit
            highest_priority_process.remaining_time -= 1

            gantt.append((highest_priority_process.pid, start_time, current_time))

            # If the process has finished its remaining time
            if highest_priority_process.remaining_time == 0:
                completed += 1
                highest_priority_process.completion_time = current_time
                highest_priority_process.turnaround_time = highest_priority_process.completion_time - highest_priority_process.arrival_time
                highest_priority_process.waiting_time = highest_priority_process.turnaround_time - highest_priority_process.burst_time
                print(f"Process {highest_priority_process.pid}: Completion Time = {highest_priority_process.completion_time}, "
                      f"Turnaround Time = {highest_priority_process.turnaround_time}, Waiting Time = {highest_priority_process.waiting_time}")
        else:
            # If no processes are available, increment time
            current_time += 1

    draw_gantt_chart(gantt)

def draw_gantt_chart(gantt):
    fig, gnt = plt.subplots()
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Process ID')

    # Create labels for each process (P1, P2, etc.)
    gnt.set_yticks([i for i in range(len(gantt))])
    gnt.set_yticklabels([f'P{g[0]}' for g in gantt])

    # Draw the Gantt chart bars
    for idx, (pid, start, end) in enumerate(gantt):
        gnt.broken_barh([(start, end - start)], (idx - 0.4, 0.8), facecolors='tab:blue')

    plt.show()

# Example
processes = [Process(1, 0, 6, 2), Process(2, 1, 8, 1), Process(3, 2, 7, 3)]
priority_preemptive(processes)
