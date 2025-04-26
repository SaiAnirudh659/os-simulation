# tests/test_round_robin.py

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/process_scheduling')))

from round_robin import round_robin_scheduling

def test_round_robin_basic():
    processes = [
        ('P1', 0, 5),
        ('P2', 1, 3),
        ('P3', 2, 1),
        ('P4', 3, 2)
    ]
    time_quantum = 2

    expected_completion_times = {
        'P1': 11,
        'P2': 10,
        'P3': 5,
        'P4': 7
    }

    schedule = round_robin_scheduling(processes, time_quantum)

    for process in schedule:
        pid = process['ProcessID']
        assert process['CompletionTime'] == expected_completion_times[pid], f"Failed for {pid}"

    print("✅ Round Robin basic test passed!")

if __name__ == "__main__":
    test_round_robin_basic()
