class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        
        count=0
        for i in nums:
            if (i&1)==0:
                count+=1
            if count>=2:
                return True
        return False