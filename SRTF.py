def srtr(processes):
    n = len(processes)
    processes.sort(key=lambda x: x['arrival_time'])  # Sort by arrival time

    remaining_times = {p['pid']: p['burst_time'] for p in processes}
    complete = 0
    current_time = 0
    last_pid = None

    # Add extra fields to each process
    for p in processes:
        p['start_time'] = -1  # To record first time it started
        p['completion_time'] = 0

    while complete != n:
        # Find process with minimum remaining time at current time
        available = [p for p in processes if p['arrival_time'] <= current_time and remaining_times[p['pid']] > 0]

        if available:
            available.sort(key=lambda x: (remaining_times[x['pid']], x['arrival_time']))
            current_process = available[0]

            # Record first start time
            if current_process['start_time'] == -1:
                current_process['start_time'] = current_time

            # Execute for 1 unit
            remaining_times[current_process['pid']] -= 1
            current_time += 1

            # If process finished
            if remaining_times[current_process['pid']] == 0:
                complete += 1
                current_process['completion_time'] = current_time
        else:
            current_time += 1  # No process available, CPU idle

    # After simulation, calculate turnaround and waiting times
    for p in processes:
        p['turnaround_time'] = p['completion_time'] - p['arrival_time']
        p['waiting_time'] = p['turnaround_time'] - p['burst_time']

    return processes

def average_times(processes):
    total_turnaround_time = sum(p['turnaround_time'] for p in processes)
    total_waiting_time = sum(p['waiting_time'] for p in processes)
    n = len(processes)

    average_turnaround_time = total_turnaround_time / n
    average_waiting_time = total_waiting_time / n

    return average_turnaround_time, average_waiting_time

# Example
processes_srtf = [
    {'pid': 'P1', 'arrival_time': 0, 'burst_time': 8},
    {'pid': 'P2', 'arrival_time': 1, 'burst_time': 4},
    {'pid': 'P3', 'arrival_time': 2, 'burst_time': 9},
    {'pid': 'P4', 'arrival_time': 3, 'burst_time': 5},
]

result = srtr(processes_srtf)
average_turnaround, average_waiting = average_times(result)

print("SJF Preemptive (SRTF) Scheduling:")
print(f"{'PID':<5} {'Arrival':<8} {'Burst':<6} {'Start':<6} {'Completion':<11} {'Turnaround':<11} {'Waiting':<7}")
for p in result:
    print(f"{p['pid']:<5} {p['arrival_time']:<8} {p['burst_time']:<6} {p['start_time']:<6} {p['completion_time']:<11} {p['turnaround_time']:<11} {p['waiting_time']:<7}")

print(f"\nAverage Turnaround Time: {average_turnaround:.2f}")
print(f"Average Waiting Time: {average_waiting:.2f}")