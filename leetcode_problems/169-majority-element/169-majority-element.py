class Solution:
    def majorityElement(self, nums):
        majority=nums[0]
        count=1
        for i in range(len(nums)):
            if nums[i]==majority:
                count+=1
            else:
                count-=1
                if count==0:
                    majority=nums[i]
                    count=1
        return majority