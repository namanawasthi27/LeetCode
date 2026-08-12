class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)<len(t):
            return False
        d={}
        j={}
        for i in range(0,len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        for i in range(0,len(t)):
            if t[i] in j:
                j[t[i]]+=1
            else:
                j[t[i]]=1   
        if d==j:
            return True
        else:
            return False