### 0/1 subset-sum counting ###

n, bar, target = map(int, input().split())
plates = list(map(int, input().split()))

# Each selected pair adds twice its plate weight.
capacity = (target - bar) // 2
ways = [0] * (capacity + 1)
ways[0] = 1  # Empty selection counts as 1

for weight in plates:
    # Work backwards so each labelled pair is used at most once.
    for total in range(capacity, weight - 1, -1):
        ways[total] += ways[total - weight]

# Find the largest achievable weight on one end.
best = capacity
while ways[best] == 0:
    best -= 1

print(bar + 2 * best, ways[best])