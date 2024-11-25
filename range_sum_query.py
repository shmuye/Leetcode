class NumArray:

    def __init__(self,nums):
        n = len(nums)
        self.prefix = [0]*n
        for i in range(1,n):
            self.prefix[i] = nums[i] + self.prefix[i - 1]
        
    def sumRange(self,left,right):
        if left == 0:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left - 1]

