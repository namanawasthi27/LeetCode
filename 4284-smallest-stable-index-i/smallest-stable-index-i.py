class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        n=len(nums)
        for i in range(0,n):
            ins=max(nums[0:i+1])-min(nums[i:n])
            if ins<=k:
                return i
        return -1
        

