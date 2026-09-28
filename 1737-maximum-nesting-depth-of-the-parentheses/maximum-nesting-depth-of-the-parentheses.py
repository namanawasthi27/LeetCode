class Solution:
    def maxDepth(self, s: str) -> int:
        openn=0
        ans=0
        for i in range(len(s)):
            if s[i]=='(':
                openn+=1
                ans=max(openn,ans)
            elif s[i]==')':
                openn-=1
        return ans