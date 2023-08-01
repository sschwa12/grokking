import math


def square(arr):
    return sorted([n ** 2 for n in arr])

def square_without_sorted(arr):
    output = [0] * len(arr)
    l, r = 0, len(arr) - 1
    next_largest_index = len(arr) - 1
    while l <= r:
        square_l, square_r = l ** 2, r ** 2
        if square_r > square_l:
            output[next_largest_index] = square_r
            r -= 1
        elif square_r <= square_l:
            output[next_largest_index] = square_l
            l += 1

        next_largest_index -= 1
    return output


assert square([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9]
assert square([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9]