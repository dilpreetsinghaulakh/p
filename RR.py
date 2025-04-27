def round_robin(processes, time_quantum):
    """Round Robin Scheduling."""
    n = len(processes)
    processes.sort(key=lambda x: x['arrival_time'])

    queue = []
    current_time = 0
    completed = []
    remaining_times = {p['pid']: p['burst_time'] for p in processes}
    arrived = []

    while len(completed) < n:
        # Add newly arrived processes
        for p in processes:
            if p not in arrived and p['arrival_time'] <= current_time:
                queue.append(p)
                arrived.append(p)

        if not queue:
            current_time += 1
            continue

        current_process = queue.pop(0)

        # Record start time if it's the first time
        if 'start_time' not in current_process:
            current_process['start_time'] = current_time

        if remaining_times[current_process['pid']] > time_quantum:
            # Execute for time quantum
            current_time += time_quantum
            remaining_times[current_process['pid']] -= time_quantum
        else:
            # Execute for remaining time and complete
            current_time += remaining_times[current_process['pid']]
            remaining_times[current_process['pid']] = 0
            current_process['completion_time'] = current_time
            current_process['turnaround_time'] = current_process['completion_time'] - current_process['arrival_time']
            current_process['waiting_time'] = current_process['turnaround_time'] - current_process['burst_time']
            completed.append(current_process)

        # Check if new processes arrived during execution
        for p in processes:
            if p not in arrived and p['arrival_time'] <= current_time:
                queue.append(p)
                arrived.append(p)

        # If process still not finished, add it back
        if current_process not in completed and current_process not in queue:
            queue.append(current_process)

    return completed

def average_times(processes):
    total_turnaround = sum(p['turnaround_time'] for p in processes)
    total_waiting = sum(p['waiting_time'] for p in processes)
    n = len(processes)

    return total_turnaround / n, total_waiting / n

def print_process_table(processes, title):
    """Print formatted table for processes."""
    print(f"\n{title}")
    print(f"{'PID':<5} {'Arrival':<8} {'Burst':<6} {'Start':<6} {'Completion':<11} {'Turnaround':<11} {'Waiting':<7}")
    for p in processes:
        print(f"{p['pid']:<5} {p['arrival_time']:<8} {p['burst_time']:<6} {p['start_time']:<6} {p['completion_time']:<11} {p['turnaround_time']:<11} {p['waiting_time']:<7}")

    avg_turnaround, avg_waiting = average_times(processes)
    print(f"\nAverage Turnaround Time: {avg_turnaround:.2f}")
    print(f"Average Waiting Time: {avg_waiting:.2f}")

# Example
processes_rr = [
    {'pid': 'P1', 'arrival_time': 0, 'burst_time': 5},
    {'pid': 'P2', 'arrival_time': 1, 'burst_time': 3},
    {'pid': 'P3', 'arrival_time': 2, 'burst_time': 1},
    {'pid': 'P4', 'arrival_time': 3, 'burst_time': 2},
]

time_quantum = 2

result = round_robin(processes_rr, time_quantum)
print_process_table(result, f"Round Robin Scheduling (Time Quantum = {time_quantum})")