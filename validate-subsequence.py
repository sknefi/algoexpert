# difficulty: 1/4

# array:     [5, 1, 22, 25, 6, -1, 8, 10]
# sequence:  [1, 6, -1, 10]
# output:    true
def isValidSubsequence(array, sequence):
    if len(sequence) > len(array): return False

    pointer = 0
    for x in array:
        if pointer == len(sequence): break

        if x == sequence[pointer]:
            pointer += 1

    if pointer == len(sequence): return True

    return False
