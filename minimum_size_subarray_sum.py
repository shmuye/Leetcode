def minSubArrayLen(target,nums):
    if sum(nums) < target:
        return 0
    n = len(nums)
    res = n + 1
    start = 0
    curr_sum = 0
    for end in range(n):
        curr_sum += nums[end]
        while curr_sum >= target:
            res = min(res,end - start + 1)
            curr_sum -= nums[start]
            start += 1
    return res
