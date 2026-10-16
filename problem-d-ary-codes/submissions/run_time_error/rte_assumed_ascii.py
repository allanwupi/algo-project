import heapq

n, d = map(int, input().split())
# Count occurrences of characters
# Bug: assumed characters are restricted to ASCII instead of Unicode (causes IndexError)
counts = [0 for _ in range(256)]
for _ in range(n):
    for character in input() + '\n':
        counts[ord(character)] += 1

# Add dummy placeholder symbols to fill tree
k = 0
for count in counts:
    if count:
        k += 1
padding = (d-1) - (k-1) % (d-1) if (k-1) % (d-1) != 0 else 0
symbols = [[counts[x], chr(x)] for x in range(len(counts)) if counts[x]]
for _ in range(padding):
    symbols.append([0, '\t'])

code_lengths = [0 for _ in range(256)]
code_lengths[ord('\t')] = 0

# Count merges
heapq.heapify(symbols)
while len(symbols) > 1:
    min_d = [heapq.heappop(symbols) for _ in range(d)]
    for _, string in min_d:
        for ch in string:
            code_lengths[ord(ch)] += 1
    merged_weight = sum([x[0] for x in min_d])
    merged_node = [merged_weight, ''.join([x[1] for x in min_d])]
    heapq.heappush(symbols, merged_node)

encoded = 0
for (ascii, count) in enumerate(counts):
    encoded += code_lengths[ascii] * count
print(encoded)
