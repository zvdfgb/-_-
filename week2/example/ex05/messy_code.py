import sys
import os
from typing import List, Dict

def process_data(items: List[int]) -> Dict[str, int]:
    unused_val = 100
    total = sum(items)
    return dict(count=len(items), sum=total)

print(process_data([1, 2, 3]))
