"""Incorrect Greedy solution"""
import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n, bar, target = data[:3]
capacity = (target - bar) // 2
used = 0
for weight in sorted(data[3:], reverse=True):
    if used + weight <= capacity:
        used += weight
print(bar + 2 * used, 1)
