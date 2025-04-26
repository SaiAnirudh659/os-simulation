# src/process_scheduling/sjf.py

def sjf_scheduling(processes):
    """
    Simulates Non-Preemptive Shortest Job First Scheduling.

    Args:
    processes (list of tuples): Each tuple contains (ProcessID, ArrivalTime, BurstTime)

    Returns:
    list of dict: Contains process info with completion time, turnaround time, waiting time.
    """
    n = len(processes)
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by Arrival Time first, then Burst Time
    completed = 0
    current_time = 0
    is_completed = [False] * n
    result = []

    while completed != n:
        idx = -1
        min_burst = float('inf')

        for i in range(n):
            pid, arrival, burst = processes[i]
            if arrival <= current_time and not is_completed[i]:
                if burst < min_burst:
                    min_burst = burst
                    idx = i
                elif burst == min_burst:
                    if arrival < processes[idx][1]:
                        idx = i

        if idx != -1:
            pid, arrival, burst = processes[idx]
            start_time = current_time
            completion_time = start_time + burst
            turnaround_time = completion_time - arrival
            waiting_time = turnaround_time - burst

            result.append({
                'ProcessID': pid,
                'ArrivalTime': arrival,
                'BurstTime': burst,
                'StartTime': start_time,
                'CompletionTime': completion_time,
                'TurnaroundTime': turnaround_time,
                'WaitingTime': waiting_time
            })

            current_time = completion_time
            is_completed[idx] = True
            completed += 1
        else:
            current_time += 1  # If no process has arrived, increment time

    return result

# Sample usage
if __name__ == "__main__":
    processes = [
        ('P1', 0, 8),
        ('P2', 1, 4),
        ('P3', 2, 9),
        ('P4', 3, 5)
    ]
    schedule = sjf_scheduling(processes)
    
    print(f"{'ProcessID':<10}{'ArrivalTime':<15}{'BurstTime':<12}{'StartTime':<12}{'CompletionTime':<18}{'TurnaroundTime':<18}{'WaitingTime':<12}")
    print("-" * 95)

    for process in schedule:
        print(f"{process['ProcessID']:<10}{process['ArrivalTime']:<15}{process['BurstTime']:<12}{process['StartTime']:<12}{process['CompletionTime']:<18}{process['TurnaroundTime']:<18}{process['WaitingTime']:<12}")
