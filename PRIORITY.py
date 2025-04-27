def priority_scheduling(processes):
    """Non-Preemptive Priority Scheduling."""
    n = len(processes)
    processes.sort(key=lambda x: (x['arrival_time'], x['priority']))  # Sort initially by arrival time and priority

    completed = []
    current_time = 0
    ready_queue = []

    while len(completed) < n:
        # Add available processes to ready queue
        for p in processes:
            if p not in completed and p['arrival_time'] <= current_time and p not in ready_queue:
                ready_queue.append(p)

        if ready_queue:
            # Select process with highest priority (lowest priority number)
            ready_queue.sort(key=lambda x: x['priority'])
            current_process = ready_queue.pop(0)

            # Calculate times
            current_process['start_time'] = current_time
            current_process['completion_time'] = current_time + current_process['burst_time']
            current_process['turnaround_time'] = current_process['completion_time'] - current_process['arrival_time']
            current_process['waiting_time'] = current_process['turnaround_time'] - current_process['burst_time']

            current_time = current_process['completion_time']
            completed.append(current_process)
        else:
            # If no process has arrived yet
            current_time += 1

    return completed

def average_times(processes):
    """Calculate average turnaround and waiting times."""
    total_turnaround = sum(p['turnaround_time'] for p in processes)
    total_waiting = sum(p['waiting_time'] for p in processes)
    n = len(processes)

    return total_turnaround / n, total_waiting / n

def print_process_table(processes, title):
    """Print formatted process table."""
    print(f"\n{title}")
    print(f"{'PID':<5} {'Arrival':<8} {'Burst':<6} {'Priority':<8} {'Start':<6} {'Completion':<11} {'Turnaround':<11} {'Waiting':<7}")
    for p in processes:
        print(f"{p['pid']:<5} {p['arrival_time']:<8} {p['burst_time']:<6} {p['priority']:<8} {p['start_time']:<6} {p['completion_time']:<11} {p['turnaround_time']:<11} {p['waiting_time']:<7}")

    avg_turnaround, avg_waiting = average_times(processes)
    print(f"\nAverage Turnaround Time: {avg_turnaround:.2f}")
    print(f"Average Waiting Time: {avg_waiting:.2f}")

# Example
processes_priority = [
    {'pid': 'P1', 'arrival_time': 0, 'burst_time': 10, 'priority': 3},
    {'pid': 'P2', 'arrival_time': 2, 'burst_time': 1, 'priority': 1},
    {'pid': 'P3', 'arrival_time': 1, 'burst_time': 2, 'priority': 4},
    {'pid': 'P4', 'arrival_time': 3, 'burst_time': 1, 'priority': 2},
]

result = priority_scheduling(processes_priority)
print_process_table(result, "Priority Scheduling (Non-Preemptive)")