def threeSumClosest(nums,target):
    nums.sort()
    diff = float('inf')
    n = len(nums)
    closestSum = 0
    for i in range(n):
        left = i + 1
        right = n - 1
        while left < right: 
            curr_sum = nums[i] + nums[left] + nums[right]
            if abs(curr_sum - target) < diff:
                diff = abs(curr_sum - target)
                closestSum = curr_sum
                print(f"checking combination:,{nums[i]},{nums[left]},{nums[right]},sum: {curr_sum}")
            elif curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return curr_sum
    return closestSum
arr = [-1,2,1,-4]
target = 1
print(threeSumClosest(arr,target))
                    

