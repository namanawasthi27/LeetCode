class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        l=[0]
        for i in range(1,n+1):
            l.append(i)
        for i in range(len(l)):
            if l[i] not in nums:
                return l[i]
        