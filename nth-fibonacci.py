# difficulty: 1/4

# n:       17
# output:  987

def getNthFib(n):
    if n == 1:
        return 0

    if 2 <= n <= 3:
        return 1

    return getNthFib(n - 1) + getNthFib(n - 2)

def recursiveFib(n, memo={}):
    # base cases
    if n == 1: return 0
    if n in memo: return memo[n]
    if 2 <= n <= 3: return 1

    memo[n] = recursiveFib(n - 1, memo) + recursiveFib(n - 2, memo)

    return memo[n]
