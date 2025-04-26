# src/process_scheduling/round_robin.py

def round_robin_scheduling(processes, time_quantum):
    """
    Final Corrected Version of Round Robin Scheduling.
    """
    from collections import deque

    processes = sorted(processes, key=lambda x: x[1])  # Sort by arrival time
    n = len(processes)
    queue = deque()
    time = 0
    idx = 0
    remaining_burst = {}
    arrival_times = {}
    completed = {}
    order_of_completion = []

    for pid, arrival, burst in processes:
        remaining_burst[pid] = burst
        arrival_times[pid] = arrival

    while queue or idx < n:
        # Add newly arrived processes
        while idx < n and processes[idx][1] <= time:
            queue.append(processes[idx][0])
            idx += 1

        if queue:
            pid = queue.popleft()

            exec_time = min(time_quantum, remaining_burst[pid])
            time += exec_time
            remaining_burst[pid] -= exec_time

            # Add newly arrived processes during execution
            while idx < n and processes[idx][1] <= time:
                queue.append(processes[idx][0])
                idx += 1

            if remaining_burst[pid] == 0:
                completion_time = time
                turnaround_time = completion_time - arrival_times[pid]
                waiting_time = turnaround_time - (processes[[p[0] for p in processes].index(pid)][2])

                completed[pid] = {
                    'ProcessID': pid,
                    'ArrivalTime': arrival_times[pid],
                    'BurstTime': processes[[p[0] for p in processes].index(pid)][2],
                    'CompletionTime': completion_time,
                    'TurnaroundTime': turnaround_time,
                    'WaitingTime': waiting_time
                }
                order_of_completion.append(pid)
            else:
                queue.append(pid)
        else:
            time += 1  # No process ready, CPU idle

    result = [completed[pid] for pid in order_of_completion]

    return result
