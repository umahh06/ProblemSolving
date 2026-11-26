class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        range_sum = n* (n+1)//2
        list_sum = sum(nums)
        return range_sum - list_sum
    
