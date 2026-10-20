# Plate loading challenge
# Attempt 1 - dynamic programming (incomplete)
# (unfortunately I was unable to solve this problem in the limited time I had)

n, B, T = list(map(int, input().split()))

target = T-B  # Remove weight of empty bar
weights = [2*int(x) for x in input().split()] # We just double the weight of the plate since we add 2 at a time

# This is a dynamic programming problem with a 1D DP table
# DP[i] stores the number of possible solutions from a set of the first i-th weights
DP = [0]*n
DP[0] = 1  # base case: using 0 plates, the empty bar is the only solution (guaranteed to be below target)

# for i > 1, we take the sum of all the solutions from 0..i-1 ???
for i in range(1, n):
    for j in range(i):
        DP[i] += DP[j]

print(DP[-1])
