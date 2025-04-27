def sjf_non_preemptive(processes):
    n = len(processes)
    processes.sort(key=lambda x: x['arrival_time'])  # Sort initially by arrival time

    completed = []
    current_time = 0
    ready_queue = []

    while len(completed) < n:
        # Add all processes that have arrived by current time to ready_queue
        for p in processes:
            if p not in completed and p['arrival_time'] <= current_time:
                if p not in ready_queue:
                    ready_queue.append(p)

        if ready_queue:
            # Pick the process with the shortest burst time
            ready_queue.sort(key=lambda x: x['burst_time'])
            current_process = ready_queue.pop(0)

            # Calculate times
            start_time = current_time
            completion_time = start_time + current_process['burst_time']
            turnaround_time = completion_time - current_process['arrival_time']
            waiting_time = turnaround_time - current_process['burst_time']

            # Update the process info
            current_process['start_time'] = start_time
            current_process['completion_time'] = completion_time
            current_process['turnaround_time'] = turnaround_time
            current_process['waiting_time'] = waiting_time

            completed.append(current_process)
            current_time = completion_time
        else:
            # If no process is ready, just move time forward
            current_time += 1

    return completed

def average_times(processes):
    total_turnaround_time = sum(p['turnaround_time'] for p in processes)
    total_waiting_time = sum(p['waiting_time'] for p in processes)
    n = len(processes)

    average_turnaround_time = total_turnaround_time / n
    average_waiting_time = total_waiting_time / n

    return average_turnaround_time, average_waiting_time

# Example
processes_sjf = [
    {'pid': 'P1', 'arrival_time': 0, 'burst_time': 7},
    {'pid': 'P2', 'arrival_time': 2, 'burst_time': 4},
    {'pid': 'P3', 'arrival_time': 4, 'burst_time': 1},
    {'pid': 'P4', 'arrival_time': 5, 'burst_time': 4},
]

result = sjf_non_preemptive(processes_sjf)
average_turnaround, average_waiting = average_times(result)

print("SJF Non-Preemptive Scheduling:")
print(f"{'PID':<5} {'Arrival':<8} {'Burst':<6} {'Start':<6} {'Completion':<11} {'Turnaround':<11} {'Waiting':<7}")
for p in result:
    print(f"{p['pid']:<5} {p['arrival_time']:<8} {p['burst_time']:<6} {p['start_time']:<6} {p['completion_time']:<11} {p['turnaround_time']:<11} {p['waiting_time']:<7}")

print(f"\nAverage Turnaround Time: {average_turnaround:.2f}")
print(f"Average Waiting Time: {average_waiting:.2f}")