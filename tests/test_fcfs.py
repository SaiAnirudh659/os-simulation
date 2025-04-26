# tests/test_fcfs.py

import sys
import os

# Add src/ to path so we can import fcfs.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/process_scheduling')))

from fcfs import fcfs_scheduling

def test_fcfs_basic():
    processes = [
        ('P1', 0, 5),
        ('P2', 2, 3),
        ('P3', 4, 1)
    ]

    expected_completion_times = [5, 8, 9]
    
    schedule = fcfs_scheduling(processes)
    actual_completion_times = [process['CompletionTime'] for process in schedule]

    assert actual_completion_times == expected_completion_times, f"Expected {expected_completion_times}, but got {actual_completion_times}"

if __name__ == "__main__":
    test_fcfs_basic()
    print("✅ FCFS basic test passed!")
