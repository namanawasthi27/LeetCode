class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd=[]
        even=[]
        for i in range(1,n+1):
            even.append(2*i)
            odd.append(2*i-1)
        sumodd=sum(odd)
        sumeven=sum(even)
        mini=min(sumodd,sumeven)
        gcd=[]
        for i in range(1,mini+1):
            if sumodd%i==0 and sumeven%i==0:
                gcd.append(i)
                
            else:
                pass
        return max(gcd)



