class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        for key in d:
            if d[key]> len(nums)//2:
                return key
