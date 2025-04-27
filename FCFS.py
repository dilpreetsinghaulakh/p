# FCFS without Arrival Times

def fcfs_without_arrival(processes):
    current_time = 0
    for process in processes:
        process['start_time'] = current_time
        process['completion_time'] = current_time + process['burst_time']
        process['turnaround_time'] = process['completion_time']
        process['waiting_time'] = process['start_time']

        current_time = process['completion_time']

    return processes

def average_times(processes):
    total_turnaround_time = sum(p['turnaround_time'] for p in processes)
    total_waiting_time = sum(p['waiting_time'] for p in processes)
    n = len(processes)

    average_turnaround_time = total_turnaround_time / n
    average_waiting_time = total_waiting_time / n

    return average_turnaround_time, average_waiting_time
# Example
processes_without_arrival = [
    {'pid': 'P1', 'burst_time': 4},
    {'pid': 'P2', 'burst_time': 3},
    {'pid': 'P3', 'burst_time': 1},
]

result = fcfs_without_arrival(processes_without_arrival)
average_turnaround, average_waiting = average_times(result)
print("\nWithout Arrival Time:")
print("PID\tBurst\tStart\tCompletion\tTurnaround\tWaiting")
for p in result:
    print(f"{p['pid']}\t{p['burst_time']}\t{p['start_time']}\t{p['completion_time']}\t\t{p['turnaround_time']}\t\t{p['waiting_time']}")
print(f"\nAverage Turnaround Time: {average_turnaround:.2f}")
print(f"Average Waiting Time: {average_waiting:.2f}")