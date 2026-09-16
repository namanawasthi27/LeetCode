class Solution:
    def numSquares(self, n: int) -> int:
        p=int(n**0.5)
        l=[]
        for i in range(1,p+1):
            l.append(i*i)
        dp=[n]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            for j in l:
                if j>i:
                    break
                dp[i]=min(dp[i],dp[i-j]+1)
        return dp[n]