# Deliberately incorrect: Computes the right weight but produces wrong output.

n, bar, target = map(int, input().split())
plates = list(map(int, input().split()))

capacity = (target - bar) // 2
ways = [0] * (capacity + 1)
ways[0] = 1  
for weight in plates:
    for total in range(capacity, weight - 1, -1):
        ways[total] += ways[total - weight]
best = capacity
while ways[best] == 0:
    best -= 1
print(bar + 2 * best, 1)
