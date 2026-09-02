class Solution:
  def maxSubArray(self, nums: list[int]) -> int:
    n=len(nums)
    final=nums[0]
    summ=nums[0]
    for i in range(1,n):
        summ=max(nums[i],summ+nums[i])
        final=max(final,summ)
    return final