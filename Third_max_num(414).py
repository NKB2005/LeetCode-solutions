class Solution(object):
    def thirdMax(self, nums):
        first = None
        second = None
        third = None
        for num in nums:
            if first == num or second == num or third == num:
                continue
            if first is None or num > first:
                third = second
                second = first
                first = num
            elif second is None or num > second:
                third = second
                second = num
            elif third is None or num > third:
                third = num
        if third is none:
            return first
        else:
            return third  