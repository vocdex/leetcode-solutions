class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        new_set=set(nums)
        return (sum(new_set)*2-sum(nums))