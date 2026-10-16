n, d = map(int, input().split())
# Count occurrences of characters
counts = {}
for _ in range(n):
    for character in input() + '\n':
        counts[character] = counts.get(character, 0) + 1

# Add dummy placeholder symbols to fill tree
k = len(counts)
padding = (d-1) - (k-1) % (d-1) if (k-1) % (d-1) != 0 else 0
symbols = [[x[1], x[0]] for x in counts.items()]
for _ in range(padding):
    symbols.append([0, '\t'])

# Store number of digits in the encoding for each symbol
code_lengths = {}
for ch in counts.keys():
    code_lengths[ch] = 0
code_lengths['\t'] = 0

# Build d-ary tree and count merges
# Priority queue is implemented as a list that is sorted after every merge
while len(symbols) > 1:
    symbols.sort(reverse=True)
    min_d = [symbols.pop() for _ in range(d)]
    for _, string in min_d:
        for ch in string:
            code_lengths[ch] += 1
    merged_weight = sum([x[0] for x in min_d])
    merged_node = [merged_weight, ''.join([x[1] for x in min_d])]
    symbols.append(merged_node)

encoded = 0
for (ch, count) in counts.items():
    encoded += code_lengths[ch] * count
print(encoded)
