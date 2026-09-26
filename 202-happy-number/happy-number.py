class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            s=str(n)
            ans=0
            for i in s:
                ans+=int(i)*int(i)
            n=ans
        return True
        
        
            

