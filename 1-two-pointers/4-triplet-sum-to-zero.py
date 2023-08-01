# O[n**2]
def triple_sum(arr):
  arr.sort()
  output = []
  for i, num in enumerate(arr):
      if i > 0 and num == arr[i - 1]:
          continue
      l = i + 1
      r = len(arr) - 1
      while l < r:
          s = sum((arr[l], arr[r], num))
          if s > 0:
              r -= 1
          elif s < 0:
              l += 1
          else:
              output.append([arr[l], arr[r], num])
              l += 1
              # need to keep moving the left pointer if there's duplicates, but we don't want it to pass the right pointer
              while arr[l] == arr[l - 1] and l < r:
                  l += 1
  return output

print(triple_sum([-3, 0, 1, 2, -1, 1, -2]))
