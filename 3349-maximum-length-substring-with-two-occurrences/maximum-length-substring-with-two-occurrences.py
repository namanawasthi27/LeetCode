class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        d={}
        left=0
        ans=0
        for right in range(len(s)):
            if s[right] in d:
                d[s[right]]+=1
            else:
                d[s[right]]=1
            while d[s[right]]>2:
                d[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans