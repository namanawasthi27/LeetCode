class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        
        n=len(nums)
        for i in range(n):
            
            for j in range(i+1,n):
                
                s=str(bin(nums[i]|nums[j])[2:])
                if s[-1]=="0":
                    return True
    
        return False