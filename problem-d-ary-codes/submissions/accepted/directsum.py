import heapq

n, d = map(int, input().split())
# Count occurrences of characters
counts = {}
for _ in range(n):
    for character in input() + '\n':
        counts[character] = counts.get(character, 0) + 1

# Add dummy symbols of frequency 0 to fill tree
k = len(counts)
padding = (d-1) - (k-1) % (d-1) if (k-1) % (d-1) != 0 else 0
symbols = [x[1] for x in counts.items()]
for _ in range(padding):
    symbols.append(0)

# Build d-ary tree and count merges
encoded = 0
heapq.heapify(symbols)
while len(symbols) > 1:
    min_d = [heapq.heappop(symbols) for _ in range(d)]
    merged_weight = sum(min_d)
    # Compute encoded length directly by adding the sum of extracted frequencies at each merge
    encoded += merged_weight
    heapq.heappush(symbols, merged_weight)

print(encoded)
