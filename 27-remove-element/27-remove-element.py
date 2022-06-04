class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nextElement=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[nextElement]=nums[i]
                nextElement+=1
        return nextElement
        