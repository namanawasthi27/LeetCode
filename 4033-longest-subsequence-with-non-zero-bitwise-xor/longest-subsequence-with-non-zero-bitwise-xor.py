class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        
        n=len(nums)
        xor=0
        for i in nums:
            xor^=i
        if xor!=0:
            return n
        else:
            for i in nums:
                if i!=0:
                    return n-1
        return 0