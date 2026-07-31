class Solution:
    def minimumPushes(self, word: str) -> int:
        d={}
        for ch in word:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        arr=list(d.values())
        arr.sort()
        arr.reverse()
        ans=0
        for i in range(0,len(arr)):
            ans+=arr[i]*(i//8+1)
        return ans