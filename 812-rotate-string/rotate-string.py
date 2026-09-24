class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        k=len(s)
        h=""
        for i in range(1,k+1):
            h=s[i:]+s[:i]
            if h==goal:
                return True
        else:
            return False
        