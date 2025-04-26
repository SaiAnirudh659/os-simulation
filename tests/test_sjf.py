# tests/test_sjf.py

import sys
import os

# Add src/ to path so we can import sjf.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/process_scheduling')))

from sjf import sjf_scheduling

def test_sjf_basic():
    processes = [
        ('P1', 0, 8),
        ('P2', 1, 4),
        ('P3', 2, 9),
        ('P4', 3, 5)
    ]

    # Expected completion order is P1 -> P2 -> P4 -> P3
    expected_completion_times = {
        'P1': 8,
        'P2': 12,
        'P4': 17,
        'P3': 26
    }

    schedule = sjf_scheduling(processes)
    
    for process in schedule:
        pid = process['ProcessID']
        assert process['CompletionTime'] == expected_completion_times[pid], f"Failed for {pid}"

    print("✅ SJF basic test passed!")

if __name__ == "__main__":
    test_sjf_basic()
