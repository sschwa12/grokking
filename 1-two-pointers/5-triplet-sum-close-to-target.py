from math import inf


def triplet_target(arr, target):
    arr.sort()
    closest_distance = float('inf')
    closest_sum = float('inf')
    for i, num in enumerate(arr):
        l = i + 1
        r = len(arr) - 1
        while l < r:
          s = arr[l] + arr[r] + num
          distance_from_target = abs(target - s)
          if distance_from_target == 0:
              return s
          if distance_from_target < closest_distance:
              
    return closest_sum

# print(triplet_target([-1, 0, 2, 3], 3))
print(triplet_target([-3, -1, 1, 2], 1))
