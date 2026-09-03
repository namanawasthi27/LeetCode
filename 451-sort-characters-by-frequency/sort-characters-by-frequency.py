class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=""
        d=dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        for key, value in d.items():
            ans+=key*value
        return ans