class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq={}
        l=[]
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        for i in range(len(nums)):
            if freq[nums[i]]==1 and nums[i]-1 not in freq and nums[i]+1 not in freq:
                l.append(nums[i])
        return l 