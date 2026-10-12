class Solution:
    def maxDepth(self, s: str) -> int:
        openn=0
        maxx=0
        for i in range(len(s)):
            if s[i]=='(':
                openn+=1
                maxx=max(maxx,openn)
            elif s[i]==')':
                openn-=1
        return maxx
            