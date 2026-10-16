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

# No dummy symbols are added

# Count merges
heapq.heapify(symbols)
while len(symbols) > 1:
    # Taking the minimum of len(symbols) prevents an IndexError but does not build a full d-ary tree, so the encoding is not optimal.
    min_d = [heapq.heappop(symbols) for _ in range(min(d, len(symbols)))]
    for _, string in min_d:
        for ch in string:
            code_lengths[ch] += 1
    merged_weight = sum([x[0] for x in min_d])
    merged_node = [merged_weight, ''.join([x[1] for x in min_d])]
    heapq.heappush(symbols, merged_node)

encoded = 0
for (ch, count) in counts.items():
    encoded += code_lengths[ch] * count
print(encoded)
