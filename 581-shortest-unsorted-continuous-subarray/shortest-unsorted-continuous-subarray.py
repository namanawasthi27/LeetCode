class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        if nums==sorted(nums):
            return 0
        elif len(nums)==1:
            return 0
        j=sorted(nums)
        left=0
        right=(len(nums))-1
        while nums[left]==j[left]:
            left+=1
        while nums[right]==j[right]:
            right-=1
        return right-left+1