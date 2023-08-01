def find_max_sum_sub_array(k, arr):
    window_start = 0
    max_sum = 0
    cur_sum = 0
    for window_end in range(len(arr)):
        cur_sum += arr[window_end]
        if window_end >= k - 1:
            max_sum = max(cur_sum, max_sum)
            cur_sum -= arr[window_start]
            window_start += 1
    return max_sum
