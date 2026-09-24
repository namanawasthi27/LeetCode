class Solution:
    def longestPalindrome(self, s: str) -> int:
        count={}
        for i in s:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        ans=0
        odd=0
        for i in count:
            if count[i]%2==0:
                ans+=count[i]
            else:
                ans+=count[i]-1
                odd=1
        return ans+odd
                    
        