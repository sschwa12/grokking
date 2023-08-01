from typing import List

# O(n) time, O(1) space
def pair_with_target_sum(arr: List[int], target: int):
  l = 0
  r = len(arr) - 1
  while l < r:
    s = arr[l] + arr[r]
    if s == target:
      return [l, r]
    if s > target:
      r -= 1
    elif s < target:
      l += 1
  return [-1, -1]

# O(n) time, O(n) space (hashmap)
def pair_with_target_sum_hash_table(arr: List[int], target: int):
  nums = {}  # to store numbers and their indices
  for i, num in enumerate(arr):
    if target - num in nums:
      return [nums[target- num], i]
    else:
      nums[num] = i
  return [-1, -1]


assert pair_with_target_sum([1, 2, 3, 4, 6], 6) == [1, 3]
assert pair_with_target_sum([2, 5, 9, 11], 11) == [0, 2]
assert pair_with_target_sum_hash_table([1, 2, 3, 4, 6], 6) == [1, 3]
assert pair_with_target_sum_hash_table([2, 5, 9, 11], 11) == [0, 2]