# src/process_scheduling/priority.py

def priority_scheduling(processes):
    """
    Simulates Non-Preemptive Priority Scheduling.

    Args:
    processes (list of tuples): Each tuple contains (ProcessID, ArrivalTime, BurstTime, Priority)

    Returns:
    list of dict: Contains process info with completion time, turnaround time, waiting time.
    """
    n = len(processes)
    completed = 0
    current_time = 0
    is_completed = [False] * n
    result = []

    while completed != n:
        idx = -1
        highest_priority = float('inf')

        for i in range(n):
            pid, arrival, burst, priority = processes[i]
            if arrival <= current_time and not is_completed[i]:
                if priority < highest_priority:
                    highest_priority = priority
                    idx = i
                elif priority == highest_priority:
                    if arrival < processes[idx][1]:
                        idx = i

        if idx != -1:
            pid, arrival, burst, priority = processes[idx]
            start_time = current_time
            completion_time = start_time + burst
            turnaround_time = completion_time - arrival
            waiting_time = turnaround_time - burst

            result.append({
                'ProcessID': pid,
                'ArrivalTime': arrival,
                'BurstTime': burst,
                'Priority': priority,
                'StartTime': start_time,
                'CompletionTime': completion_time,
                'TurnaroundTime': turnaround_time,
                'WaitingTime': waiting_time
            })

            current_time = completion_time
            is_completed[idx] = True
            completed += 1
        else:
            current_time += 1

    return result

# Sample usage
if __name__ == "__main__":
    processes = [
        ('P1', 0, 4, 2),
        ('P2', 1, 3, 1),
        ('P3', 2, 1, 3),
        ('P4', 3, 2, 2)
    ]
    schedule = priority_scheduling(processes)
    
    print(f"{'ProcessID':<10}{'ArrivalTime':<15}{'BurstTime':<12}{'Priority':<10}{'StartTime':<12}{'CompletionTime':<18}{'TurnaroundTime':<18}{'WaitingTime':<12}")
    print("-" * 110)

    for process in schedule:
        print(f"{process['ProcessID']:<10}{process['ArrivalTime']:<15}{process['BurstTime']:<12}{process['Priority']:<10}{process['StartTime']:<12}{process['CompletionTime']:<18}{process['TurnaroundTime']:<18}{process['WaitingTime']:<12}")
