# Exhaustive search: exponential without memoization.

n, bar, target = map(int, input().split())
plates = list(map(int, input().split()))

capacity = (target - bar) // 2
best = -1
count = 0


def visit(index, total):
    global best, count

    # All pairs have been considered
    if index == n:
        if total > best:
            best = total
            count = 1
        elif total == best:
            count += 1
        return

    # Do not use this pair.
    visit(index + 1, total)

    # Use this pair if it fits.
    if total + plates[index] <= capacity:
        visit(index + 1, total + plates[index])


visit(0, 0)
print(bar + 2 * best, count)