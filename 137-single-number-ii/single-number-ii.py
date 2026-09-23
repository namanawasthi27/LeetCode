class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        for key, values in d.items():
            if values==1:
                return key