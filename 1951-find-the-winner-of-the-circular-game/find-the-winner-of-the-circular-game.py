class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[]
        for i in range(1,n+1):
            l.append(i)
        pos=0
        while len(l)>1:
            pos=(pos+k-1)%len(l)
            l.pop(pos)
        return l[0]
            
