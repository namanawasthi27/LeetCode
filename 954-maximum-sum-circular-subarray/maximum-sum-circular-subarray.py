class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        n=len(nums)
        total=sum(nums)
        minsum=nums[0]
        maxsum=nums[0]
        currmin=nums[0]
        currmax=nums[0]
        for i in range(1,n):
            currmax=max(nums[i],currmax+nums[i])
            maxsum=max(currmax,maxsum)
            currmin=min(nums[i],currmin+nums[i])
            minsum=min(currmin,minsum)
        if maxsum<0:
            return maxsum
        return max(maxsum,total-minsum)