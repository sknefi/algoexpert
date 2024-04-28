# difficulty: 1/4

# array:  [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
# target:  33

# output:  33

def binarySearch(array, target):
    left: int = 0
    right: int = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid

        elif array[mid] < target:
            left = mid + 1

        elif array[mid] > target:
            right = mid - 1

    return -1  # value is not in list