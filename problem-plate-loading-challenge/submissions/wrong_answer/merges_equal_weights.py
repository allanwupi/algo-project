# Incorrectly merges equal weights

n, bar, target = map(int, input().split())
plates = list(map(int, input().split()))

capacity = (target - bar) // 2
ways = [0] * (capacity + 1)
ways[0] = 1  # Counts as 1 for no selection
for weight in sorted(set(plates)): # set(plates) removes equal-weight pairs
    for total in range(capacity, weight - 1, -1):
        ways[total] += ways[total - weight]
best = capacity
while ways[best] == 0:
    best -= 1
print(bar + 2 * best, ways[best])