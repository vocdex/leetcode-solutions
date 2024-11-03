class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        new_set=set(nums)
        return(sum(new_set)*3-sum(nums))//2
        