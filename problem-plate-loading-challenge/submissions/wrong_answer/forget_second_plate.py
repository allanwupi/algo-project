# Treats a pair as one plate and forgets the other end.

n, bar, target = map(int, input().split())
plates = list(map(int, input().split()))

capacity = target - bar
ways = [0] * (capacity + 1)
ways[0] = 1  
for weight in plates:
    for total in range(capacity, weight - 1, -1):
        ways[total] += ways[total - weight]
best = capacity
while ways[best] == 0:
    best -= 1
print(bar + best, ways[best])
