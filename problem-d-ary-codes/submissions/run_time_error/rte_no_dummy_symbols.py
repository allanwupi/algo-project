import heapq

n, d = map(int, input().split())
# Count occurrences of characters
counts = {}
for _ in range(n):
    for character in input() + '\n':
        counts[character] = counts.get(character, 0) + 1

symbols = [[x[1], x[0]] for x in counts.items()]

code_lengths = {}
for ch in counts.keys():
    code_lengths[ch] = 0

# No dummy symbols are added (sample cases 1 and 2 still pass)

# Count merges
heapq.heapify(symbols)
while len(symbols) > 1:
    min_d = [heapq.heappop(symbols) for _ in range(d)] # results in IndexError on secret test cases
    for _, string in min_d:
        for ch in string:
            code_lengths[ch] += 1
    merged = [sum([x[0] for x in min_d]), ''.join([x[1] for x in min_d])]
    heapq.heappush(symbols, merged)

encoded = 0
for (ch, count) in counts.items():
    encoded += code_lengths[ch] * count
print(encoded)
