class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        i=n+1
        while True:
            arr = [int(j) for j in str(i)]
            d={}
            for j in arr:
                if j in d:
                    d[j]+=1
                else:
                    d[j]=1
            for j in d:
                if d[j]!=j:
                    break
            else:
                return i
            i=i+1
