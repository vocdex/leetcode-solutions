import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum=0
        min_len=math.inf
        window_start=0
        for i in range(len(nums)):
            window_sum+=nums[i]
            while window_sum>=target:
                min_len=min(min_len,i-window_start+1)
                window_sum-=nums[window_start]
                window_start+=1
        if min_len==math.inf:
            return 0
        return min_len        