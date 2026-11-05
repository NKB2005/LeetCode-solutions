class Solution(object):
    def pivotIndex(self, nums):
        for i in range(len(nums)):
            left_sum = sum(nums[0:i])
            right_sum = sum(nums[i+1:])
            if left_sum == right_sum:
                return i
        return -1
        