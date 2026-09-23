class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target=sum(nums)-x
        l=0
        s=0
        ans=-1
        for r in range(len(nums)):
            s+=nums[r]
            while s>target and l<=r:
                s-=nums[l]
                l+=1
            if s==target:
                ans=max(ans,r-l+1)
        if ans==-1:
            return -1
        return len(nums)-ans