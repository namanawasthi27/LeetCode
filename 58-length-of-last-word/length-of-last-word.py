class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=s.split()
        return len(i[-1])
        
        
        
        