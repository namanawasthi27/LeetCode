class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.upper()
        l=[]
        ans=""
        for i in range(len(s)):
            if s[i]=="-":
                pass
            else:
                l.append(s[i])
        if len(s)<=k:
            for i in range(len(l)):
                ans+=l[i]
            return ans
        rem=len(l)%k
        ans=""
        if rem!=0:
            for i in range(rem):
                ans+=l[i]
            ans+="-"
        for i in range(rem,len(l),k):
            for j in range(i,i+k):
                ans+=l[j]
            if i+k<len(l):
                ans+="-"
        return ans
        
        