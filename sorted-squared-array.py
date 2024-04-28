# difficulty: 1/4


# array:   [-3, -2, -1]
# output:  [1, 4, 9]

def powerOfTwo(x: int):
    return x * x


def sortedSquaredArray(array):
    n = len(array)
    left = 0
    right = len(array) - 1
    writer = len(array) - 1

    result = [0] * n
    while left <= right:
        if abs(array[left]) < abs(array[right]):
            result[writer] = powerOfTwo(abs(array[right]))
            right -= 1
        else:
            result[writer] = powerOfTwo(abs(array[left]))
            left += 1

        writer -= 1

    return result
