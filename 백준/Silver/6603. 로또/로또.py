from itertools import combinations
import sys

first = True
for line in sys.stdin:
    if line.startswith('0'): break
    if not first: print()
    
    data = list(map(int, line.split()))
    for comb in combinations(data[1:], 6):
        print(*comb)
    first = False