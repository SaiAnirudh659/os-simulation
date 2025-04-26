# tests/test_priority.py

import sys
import os

# Add src/ to path so we can import priority.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/process_scheduling')))

from priority import priority_scheduling

def test_priority_basic():
    processes = [
        ('P1', 0, 4, 2),
        ('P2', 1, 3, 1),
        ('P3', 2, 1, 3),
        ('P4', 3, 2, 2)
    ]

    expected_completion_times = {
        'P1': 4,
        'P2': 7,
        'P4': 9,
        'P3': 10
    }

    schedule = priority_scheduling(processes)

    for process in schedule:
        pid = process['ProcessID']
        assert process['CompletionTime'] == expected_completion_times[pid], f"Failed for {pid}"

    print("✅ Priority Scheduling basic test passed!")

if __name__ == "__main__":
    test_priority_basic()
