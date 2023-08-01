# O(n * k) time O(1) space
# complexity of .pop(k) is O(k)
def remove_duplicates(arr):
  l = 0
  r = 1
  while r < len(arr):
    if arr[l] == arr[r]:
      arr.pop(r)
    else:
      l += 1
      r += 1
  return len(arr)

  [2, 3, 3, 3, 6, 9, 9]

# better way, without popping from list
# O(n) time O(1) space
def remove_duplicates_another_way(arr):
  next_non_duplicate = 1
  i = 0
  while i < len(arr):
    if arr[i] != arr[next_non_duplicate]:
      arr[next_non_duplicate] = arr[i]
      next_non_duplicate += 1
    i += 1
    

assert remove_duplicates([2, 3, 3, 3, 6, 9, 9]) == 4
assert remove_duplicates([2, 2, 2, 11]) == 2
assert remove_duplicates_another_way([2, 3, 3, 3, 6, 9, 9]) == 4
assert rremove_duplicates_another_way([2, 2, 2, 11]) == 2