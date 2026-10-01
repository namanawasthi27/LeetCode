class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        count={}
        maxx=0
        ans=0
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]]+=1
            else:
                count[s[right]]=1
            maxx=max(maxx,count[s[right]])
            while (right-left+1)-maxx>k:
                count[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans