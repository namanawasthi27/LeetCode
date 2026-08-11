class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        count=0
        ans=len(nums)+1
        for right in range(len(nums)):
            count+=nums[right]
            while count>=target:
                ans=min(ans,right-left+1)
                count-=nums[left]
                left+=1
        if ans>=len(nums)+1:
            return 0
        return ans