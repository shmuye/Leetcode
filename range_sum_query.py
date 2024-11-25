class NumArray:

    def __init__(self,nums):
        n = len(nums)
        self.prefix = [0]*n
        for i in range(1,n):
            self.prefix[i] = nums[i] + self.prefix[i - 1]
        return self.prefix
    def sumRange(self,left,right):
