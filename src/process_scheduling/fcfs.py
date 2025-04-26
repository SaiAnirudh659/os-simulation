# src/process_scheduling/fcfs.py

def fcfs_scheduling(processes):
    """
    Simulates First Come First Serve Scheduling.

    Args:
    processes (list of tuples): Each tuple contains (ProcessID, ArrivalTime, BurstTime)

    Returns:
    list of dict: Contains process info with completion time, turnaround time, waiting time.
    """
    # Sort by Arrival Time
    processes.sort(key=lambda x: x[1])
    
    current_time = 0
    result = []

    for pid, arrival, burst in processes:
        if current_time < arrival:
            current_time = arrival
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

    return result

# Sample usage
if __name__ == "__main__":
    processes = [
        ('P1', 0, 5),
        ('P2', 2, 3),
        ('P3', 4, 1)
    ]
    schedule = fcfs_scheduling(processes)
    
    # Table Header
    print(f"{'ProcessID':<10}{'ArrivalTime':<15}{'BurstTime':<12}{'StartTime':<12}{'CompletionTime':<18}{'TurnaroundTime':<18}{'WaitingTime':<12}")
    print("-" * 95)

    # Table Rows
    for process in schedule:
        print(f"{process['ProcessID']:<10}{process['ArrivalTime']:<15}{process['BurstTime']:<12}{process['StartTime']:<12}{process['CompletionTime']:<18}{process['TurnaroundTime']:<18}{process['WaitingTime']:<12}")

# This simple code will :
# Take a list of processes (ProcessID, Arrival Time, Burst Time)
# Perform FCFS scheduling
# Return and print Completion Time, Turnaround Time, and Waiting Time.