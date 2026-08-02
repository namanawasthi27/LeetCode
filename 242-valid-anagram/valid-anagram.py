class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s.lower()
        t.lower()
        g=sorted(s)
        f=sorted(t)
        if g==f:
            return True
        return False